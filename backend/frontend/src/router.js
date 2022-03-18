import Vue from 'vue';
import VueRouter from 'vue-router';
import home from './views/homepage.vue';
import control from './views/excel_control.vue';
import file from './views/file_download.vue';


Vue.use(VueRouter);

const routes = [{
    path: '/',
    name: 'home',
    component: home,
    meta: {
        auth: undefined
    }
},{
    path: '/ExcelControl',
    name: 'control',
    component: control,
    meta: {
        auth: undefined
    }
},{
    path: '/FileDownload',
    name: 'file',
    component: file,
    meta: {
        auth: undefined
    }
},];

const router = new VueRouter({
    routes: routes,
    linkActiveClass: 'active'
});

export default router;