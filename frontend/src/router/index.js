import { createRouter, createWebHashHistory } from 'vue-router'
import Login from  '@/pages/Login'
import SignUp from  '@/pages/SignUp'
import Home from '@/pages/Home'

const routes = [
  {
      path:'/',
      component: Home
  },
  {
      path:'/login',
      component: Login
  },
  {
      path:'/registr',
      component: SignUp
  },
  // {
  //   path:'/room',
  //   name: 'room',
  //   component: room
  // },
  // {
  //   path: '/dialog/:id',
  //   name: 'dialog',
  //   component: dialogWs
  // },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
