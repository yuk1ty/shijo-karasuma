import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import AddStock from '@/components/AddStock'
import ViewStock from '@/components/ViewStock'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
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
