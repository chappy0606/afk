import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { key, store } from './store/'
import axios from 'axios'
import VueAxios from 'vue-axios'

createApp(App)
    .use(store, key)
    .use(router)
    .use(VueAxios, axios)
    .mount('#app')
