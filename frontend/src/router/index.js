import Vue from 'vue'
import Router from 'vue-router'
import PcapAnalysis from '@/pages/Pcap-Analysis'

Vue.use(Router)

export default new Router({
  routes: [{
    path: '/',
    name: 'index',
    component: PcapAnalysis
  }]
})
