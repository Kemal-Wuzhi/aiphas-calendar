import Vue from 'vue'
import VueRouter from 'vue-router'
import NotFound from '../views/NotFound.vue'
import SignIn from '../views/SignIn.vue'
import SignUp from '../views/SignUp.vue'
import MainPage from '../views/MainPage.vue'

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
    redirect:'/mainpage'
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
    path:'/mainpage',
    name:'main-page',
    component:MainPage
  }
  
]

const router = new VueRouter({
  routes
})

export default router
