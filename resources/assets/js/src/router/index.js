import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/index/Index'
import Hello from '@/components/Hello'
import StockRegister from '@/components/stock/register/StockRegister'
import AddStock from '@/components/AddStock'
import ViewStock from '@/components/ViewStock'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/stock/register',
      name: 'StockRegister',
      component: StockRegister
    },
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/hello',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/addStock',
      name: 'AddStock',
      component: AddStock
    },
    {
      path: '/viewStock',
      name: 'ViewStock',
      component: ViewStock
    }
  ],
  mode: 'history'
})
