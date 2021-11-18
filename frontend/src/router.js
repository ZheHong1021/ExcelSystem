import Vue from 'vue';
import VueRouter from 'vue-router';
import home from './components/homepage.vue';
import control from './components/excel_control.vue';


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
},];

const router = new VueRouter({
    routes: routes,
    linkActiveClass: 'active'
});

export default router;