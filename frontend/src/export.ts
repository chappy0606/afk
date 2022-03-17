import axios from 'axios'
import { store } from '@/store'

let isRetry: boolean = false

const instance = axios.create({
    baseURL: 'https://192.168.10.11:8000/api/v1'
})

instance.interceptors.response.use(
    response => {
        return response
    },
    async error => {
        if (error.response.status === 401 && !isRetry) {
            isRetry = true

            try {
                const response = await instance.post('/auth/token/refresh/', {
                    refresh: store.state.authUser.refreshToken
                })
                store.commit('setAccessToken', response.data.access)
                error.config.headers.Authorization =
                    'JWT ' + store.state.authUser.accessToken
                
                return await axios.request(error.config)

            } catch (e) {
                if (axios.isAxiosError(e)) {
                    if (e.request.status == 401) {
                        store.dispatch('authLogout')
                    }
                }
            }
        }
        isRetry = false
        return Promise.reject(error)
    }
)

export default instance