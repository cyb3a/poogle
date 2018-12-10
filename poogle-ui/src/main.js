import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/de';
import App from './App.vue';
import './registerServiceWorker';

Vue.use(ElementUI, { locale });
Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app');
