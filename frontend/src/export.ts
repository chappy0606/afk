import axios from 'axios'
import { store } from '@/store'

axios.interceptors.response.use(
    response => {
        return response
    },
    error => {
        if (error.response.status == 401) {
            axios
                .post('https://127.0.0.1:8000/api/v1/auth/token/refresh/', {
                    refresh: store.state.authUser.refreshToken
                })
                .then(response => {
                    console.log('success token refresh')
                    store.commit('setAccessToken', response.data.access)
                    error.config.headers.Authorization = 'JWT ' + store.state.authUser.accessToken
                    return axios.request(error.config)
                })
                .catch(error => {
                    if (error.response.status == 401) {
                        // refreshToken期限切れで強制ログアウト
                        store.dispatch('authLogout')
                    }
                })
        }
        return Promise.reject(error)
    }
)

export default axios
