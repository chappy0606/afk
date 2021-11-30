import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import TopPage from '@/components/pages/TopPage.vue'
import PveComp from '@/components/pages/PveComp.vue'
import UploadPage from '@/components/pages/UploadPage.vue'
import LoginPage from '@/components/pages/LoginPage.vue'
import Registration from '@/components/pages/Registration.vue'
import Profile from '@/components/pages/Profile.vue'
import RelicCalcuator from '@/components/pages/RelicCalcuator.vue'
import { store } from '@/store'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        name: 'TopPage',
        component: TopPage
    },

    {
        path: '/login',
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
        meta: { requiresAuth: true }
    },

    {
        path: '/registration',
        name: 'Registration',
        component: Registration
    },

    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
        meta: { requiresAuth: true }
    },
    {
        path: '/relic_calcuator',
        name: 'RelicCalcuator',
        component: RelicCalcuator
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

const isLogin = () => {
    return store.state.auth.isAuth
}

const url:string[] = ['/login', '/registration']

router.beforeEach((to, from, next) => {
    if (url.includes(to.path) && isLogin()) {
        router.push({ name: 'TopPage' })
    }

    if (to.matched.some(record => record.meta.requiresAuth)) {
        store.commit('setCurrentPath', { currentPath: to.path })
        if (isLogin()) {
            next()
        } else {
            next({ name: 'Login' })
        }
    } else {
            next()
        }
})

export default router
