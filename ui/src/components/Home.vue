<script setup>
import { useRouter } from "vue-router";
const router = useRouter();
</script>
<template>
  <el-button @click="router.push('/mine')">我的信息</el-button>
  <el-button @click="router.push('/question')">我的文章</el-button>
  <el-button @click="router.push('/publish')">发布文章</el-button>
</template>
<style lang="scss"></style>
