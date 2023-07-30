import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index'
import Elementplus from 'element-plus'
import 'element-plus/dist/index.css'
import request from './utils/request'
import storage from './utils/storage'
import api from './api'

const app = createApp(App)

// 全局挂载
app.config.globalProperties.$request = request
app.config.globalProperties.$storage = storage
app.config.globalProperties.$api = api

app.use(Elementplus).use(router).mount('#app')


