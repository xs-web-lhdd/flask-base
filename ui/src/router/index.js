// 使用createWebHashHistory的好处：在上线的时候不需要nagix的配置
import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../components/Home.vue'

const routes = [
    {
        name: 'Home',
        path: '/',
        meta: {
            title: '首页'
        },
        component:Home,
    },
    {
        name: 'Login',
        path: '/login',
        meta: {
            title: '登录'
        },
        component:() => import('../views/Login.vue')
    },
    {
      name: 'Register',
      path: '/register',
      meta: {
          title: '注册'
      },
      component:() => import('../views/Register.vue')
  },
  {
    name: 'Publish',
    path: '/publish',
    meta: {
        title: '发布文章'
    },
    component:() => import('../views/Publish.vue')
  },
  {
    name: 'Mine',
    path: '/mine',
    meta: {
        title: '个人信息'
    },
    component:() => import('../views/Mine.vue')
  },
  {
    name: 'Question',
    path: '/question',
    meta: {
        title: '我的文章'
    },
    component:() => import('../views/Mine.vue')
  },
  {
      name: '404',
      path: '/404',
      meta: {
          title: '页面不存在'
      },
      component:() => import('../views/404.vue')
  }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

function checkPermission(path) {
    let hasPermission = router.getRoutes().filter(route => route.path == path).length;
    if (hasPermission) {
        return true;
    } else {
        return false;
    }
}

// 导航守卫
router.beforeEach((to, from, next) => {
    if (checkPermission(to.path)) {
        document.title = to.meta.title;
        next()
    } else {
        next('/404')
    }
})
export default router