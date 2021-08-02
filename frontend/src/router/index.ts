import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import TopPage from '@/components/pages/TopPage.vue'
import PveComp from '@/components/pages/PveComp.vue'
import UploadPage from '@/components/pages/UploadPage.vue'
import LoginPage from '@/components/pages/LoginPage.vue'
import { store } from '@/store'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        name: 'TopPage',
        component: TopPage,
    },

    {
        path: '/login',
        name: 'login',
        component: LoginPage,
    },

    {
        path: '/pve_comp',
        name: 'PveComp',
        component: PveComp,
    },

    {
        path: '/pve_comp/:id',
        name: 'ChapterStsage',
        component: PveComp,
    },
    {
        path: '/pve_comp/upload',
        name: 'Upload',
        component: UploadPage,
        meta: { isAuth: true }
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})
router.beforeEach((to, from, next) => {
    if (to.path === '/login' && store.state.auth.isAuth) {
        router.push({ path: '/' })
    }
    if (to.matched.some(record => record.meta.isAuth)) {
        store.commit('setCurrentPath', { currentPath: to.path })
        if (store.state.auth.isAuth) {
            next()
        } else {
            next('/login')
        }
    } else {
        next()
    }
})

export default router
