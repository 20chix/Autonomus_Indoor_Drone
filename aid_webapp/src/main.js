import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader
Vue.use(Vuetify);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app');
