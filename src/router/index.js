// import Vue from 'vue';
// import Router from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router'
import SearchIP from '../components/page_searchIP.vue';
import page_reconcile from '@/components/page_reconcile.vue';
// import Home_page from '../views/Home_page.vue';
// import Content_page from '../views/Content_page.vue';

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/search-ip',
      name: 'SearchIP',
      component: SearchIP
    },
    {
      path: '/reconcile/:id',
      name: 'page_reconcile',
      component: page_reconcile,
      props: true,
    }
  ]});

export default router;
