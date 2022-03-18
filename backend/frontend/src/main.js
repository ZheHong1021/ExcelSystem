import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import router from './router';
import 'vuetify/dist/vuetify.min.css'
import axios from 'axios'
import store from './store'

Vue.config.devtools=true;

Vue.prototype.$axios = axios
Vue.config.productionTip = false

Vue.use(Vuetify)

new Vue({
  vuetify: new Vuetify(),
  router,
  axios,
  store,
  render: h => h(App)
}).$mount('#app')


new Vuetify({
  icons: {
      iconfont: 'md', // 'mdi' || 'mdiSvg' || 'md' || 'fa' || 'fa4' || 'faSvg'
  },
})