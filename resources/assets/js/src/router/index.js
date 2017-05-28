import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/index/Index'
import StockRegister from '@/components/stock/register/StockRegister'
import ViewStock from '@/components/ViewStock'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/stock/register',
      name: 'StockRegister',
      component: StockRegister
    },
    {
      path: '/viewStock',
      name: 'ViewStock',
      component: ViewStock
    }
  ],
  mode: 'history'
})
