import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import TopPage from '@/components/pages/TopPage.vue'
import PveComp from '@/components/pages/PveComp.vue'
import UploadPage from '@/components/pages/UploadPage.vue'
import LoginPage from '@/components/pages/LoginPage.vue'
import Registration from '@/components/pages/Registration.vue'
import { store } from '@/store'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        name: 'TopPage',
        component: TopPage
    },

    {
        path: '/user/login',
        name: 'Login',
        component: LoginPage
    },

    {
        path: '/pve_comp',
        name: 'PveComp',
        component: PveComp
    },

    {
        path: '/pve_comp/upload',
        name: 'Upload',
        component: UploadPage,
        meta: { isAuth: true }
    },
    
    {
        path: '/user/registration',
        name: 'Registration',
        component: Registration,
        meta: {isAuth: false}
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})
router.beforeEach((to, from, next) => {
    if (to.path === '/user/login' && store.state.auth.isAuth) {
        router.push({ name: 'TopPage' })
    }
    if (to.matched.some(record => record.meta.isAuth)) {
        store.commit('setCurrentPath', { currentPath: to.path })
        if (store.state.auth.isAuth) {
            next()
        } else {
            next({ name: 'Login' })
        }
    } else {
        next()
    }
})

export default router
