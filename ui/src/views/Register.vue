<template>
  <div class="wrapper">
    <el-form
      ref="ruleFormRef"
      :model="ruleForm"
      :rules="rules"
      label-width="120px"
      class="demo-ruleForm"
      :size="formSize"
      status-icon
    >
      <el-form-item label="用户名" prop="username">
        <el-input v-model="ruleForm.username" />
      </el-form-item>
      <el-form-item label="昵称" prop="nickname">
        <el-input v-model="ruleForm.nickname" />
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="ruleForm.password" />
      </el-form-item>
      <el-form-item label="确认密码" prop="confirmpwd">
        <el-input v-model="ruleForm.confirmpwd" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm(ruleFormRef)">
          注册
        </el-button>
        <el-button @click="resetForm(ruleFormRef)">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { reactive, ref, getCurrentInstance } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";

const formSize = ref("default");
const ruleFormRef = ref();
const ruleForm = reactive({
  username: "",
  nickname: "",
  password: "",
  confirmpwd: "",
});

const rules = reactive({
  username: [{ required: true, message: "请输入用户名", trigger: "blur" }],
  nickname: [{ required: true, message: "请输入用户昵称", trigger: "blur" }],
  password: [{ required: true, message: "请设置登陆密码", trigger: "blur" }],
  confirmpwd: [{ required: true, message: "请确认密码", trigger: "blur" }],
});

// 实例化上下文对象
const { ctx, proxy } = getCurrentInstance();
const router = useRouter();

const submitForm = async (formEl) => {
  if (!formEl) return;
  await formEl.validate(async (valid, fields) => {
    if (valid) {
      const res = await proxy.$api.registerApi({ ...ruleForm });
      if (res) {
        ElMessage.success("注册成功！");
        router.push("/login");
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

<style lang="scss">
.wrapper {
  width: 800px;
  height: 800px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
