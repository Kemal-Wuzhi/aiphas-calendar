import Vue from 'vue'
import VueRouter from 'vue-router'
import NotFound from '../views/NotFound.vue'
import SignIn from '../views/SignIn.vue'
import SignUp from '../views/SignUp.vue'
import Main from '../views/Main.vue'


Vue.use(VueRouter)

const routes = [
  {
    path:'*',
    name:'not-found',
    component:NotFound,
  },
  {
    path:'/',
    name:'root',
    redirect:'/main'
  },
  {
    path:'/signin',
    name:'sign-in',
    component:SignIn
  },
  {
    path:'/signup',
    name:'sign-up',
    component:SignUp
  },
  {
    path:'/main',
    name:'main',
    component:Main
  },

  
]

const router = new VueRouter({
  routes
})

export default router
