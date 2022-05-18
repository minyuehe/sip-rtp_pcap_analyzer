import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('@/pages/Pcap-Analysis')
    },
    {
      path: '/black',
      name: 'kongbaiye',
      component: () => import('@/pages/kongbaiye')
    }
  ]
})
