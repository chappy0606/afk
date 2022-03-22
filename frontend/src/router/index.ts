import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import TopPage from '@/components/pages/TopPage.vue'
import PveComp from '@/components/pages/PveComp.vue'
import UploadPage from '@/components/pages/UploadPage.vue'
import LoginPage from '@/components/pages/LoginPage.vue'
import Registration from '@/components/pages/Registration.vue'
import Profile from '@/components/pages/Profile.vue'
import RelicCalcuator from '@/components/pages/RelicCalcuator.vue'
import NotFound from '@/components/pages/NotFound.vue'
import { store } from '@/store'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        name: 'TopPage',
        component: TopPage,
        meta: { isPublic: true }
    },

    {
        path: '/login',
        name: 'Login',
        component: LoginPage,
        meta: { isPublic: true }
    },

    {
        path: '/pve_comp',
        name: 'PveComp',
        component: PveComp,
        meta: { isPublic: true }
    },

    {
        path: '/pve_comp/upload',
        name: 'Upload',
        component: UploadPage
    },

    {
        path: '/registration',
        name: 'Registration',
        component: Registration,
        meta: { isPublic: true }
    },

    {
        path: '/profile',
        name: 'Profile',
        component: Profile
    },
    {
        path: '/relic_calcuator',
        name: 'RelicCalcuator',
        component: RelicCalcuator,
        meta: { isPublic: true }
    },

    //vue-router3と4で書き方違う
    {
        path: '/:pathMatch(.*)*',
        name: 'notFound',
        component: NotFound
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

const isLogin = () => {
    return store.state.auth.isAuth
}

router.beforeEach((to, from, next) => {
    //認証なしのページの場合
    if (to.matched.some(record => record.meta.isPublic)) {
        store.commit('setCurrentPath', { currentPath: to.path })
        next()
        if (isLogin()) {
            next({ name: 'TopPage' })
        } else {
            next()
        }
    }
    //認証ありの場合ログイン誘導
    else { 
        next({ name: 'Login' })
    }
})

export default router
