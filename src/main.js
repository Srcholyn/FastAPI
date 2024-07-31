// import Vue from 'vue';
import { createApp } from 'vue'
import App from './App.vue';
import router from './router';
import { VueDragscroll  } from "vue-dragscroll";




createApp(App).use(router, VueDragscroll).mount('#app')
