import { createStore } from 'vuex'

export interface token{
  accsesToken: string
  refreshToken: string
}

export default createStore({
  state: {
    accsesToken: '',
    refreshToken:'',
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
