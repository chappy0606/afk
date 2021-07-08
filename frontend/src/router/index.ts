import { createRouter, createWebHistory, RouteRecordRaw} from 'vue-router'
import TopPage from '@/components/pages/TopPage.vue'
import PveComp from '@/components/pages/PveComp.vue'
import UploadPage from '@/components/pages/UploadPage.vue'
import LoginPage from '@/components/pages/LoginPage.vue'

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
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
// router.beforeEach()

export default router