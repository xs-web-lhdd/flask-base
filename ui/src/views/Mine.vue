<script setup>
import { reactive, ref, getCurrentInstance } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { Plus } from "@element-plus/icons-vue";

const formSize = ref("default");
const ruleFormRef = ref();
const ruleForm = reactive({
  username: "",
  password: "",
});
const imageUrl = ref("");

const uploadRef = ref();

// const rules = reactive({
//   username: [{ required: true, message: "请输入用户名", trigger: "blur" }],
//   password: [{ required: true, message: "请设置登陆密码", trigger: "blur" }],
// });

// 实例化上下文对象
const { ctx, proxy } = getCurrentInstance();
const router = useRouter();

const beforeAvatarUpload = (rawFile) => {
  if (rawFile.type !== "image/jpeg") {
    ElMessage.error("头像格式必须是 JPG!");
    return false;
  } else if (rawFile.size / 1024 / 1024 > 2) {
    ElMessage.error("头像大小不能超过 2MB");
    return false;
  }
  return true;
};

const handleAvatarSuccess = (response, uploadFile) => {
  if (response.code === 200) ElMessage.success(response.message);
  imageUrl.value = URL.createObjectURL(uploadFile.raw);
};

const submitForm = async (formEl) => {
  if (!formEl) return;
  await formEl.validate(async (valid, fields) => {
    if (valid) {
      const res = await proxy.$api.loginApi({ ...ruleForm });
      if (res) {
        ElMessage.success("登陆成功！");
        router.push("/");
      }
    } else {
      console.log("error submit!", fields);
    }
  });
};

const resetForm = (formEl) => {
  if (!formEl) return;
  formEl.resetFields();
};
</script>
<template>
  <div class="wrapper">
    <el-form
      ref="ruleFormRef"
      :model="ruleForm"
      label-width="120px"
      class="demo-ruleForm"
      :size="formSize"
      status-icon
    >
      <el-form-item>
        <el-upload
          ref="uploadRef"
          class="avatar-uploader"
          action="/api/accounts/upload"
          method="post"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"
        >
          <img v-if="imageUrl" :src="imageUrl" class="avatar" />
          <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
        </el-upload>
      </el-form-item>
      <el-form-item label="用户名" prop="username">
        <el-input v-model="ruleForm.username" />
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="ruleForm.password" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm(ruleFormRef)">
          登陆
        </el-button>
        <el-button @click="resetForm(ruleFormRef)">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<style lang="scss">
.wrapper {
  width: 800px;
  // height: 800px;
  margin: 0 auto;
  // display: flex;
  // align-items: center;
  // justify-content: center;
}
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}
</style>
