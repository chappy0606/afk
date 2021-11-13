import axios from 'axios'
import { store } from '@/store'

let isRetry: boolean = false

axios.interceptors.response.use(
    response => {
        return response
    },
    async error => {
        if (error.response.status === 401 && !isRetry) {
            isRetry = true

            try {
                const response = await axios.post(
                    'https://127.0.0.1:8000/api/v1/auth/token/refresh/',
                    {
                        refresh: store.state.authUser.refreshToken
                    }
                )
                console.log('tryさん')
                store.commit('setAccessToken', response.data.access)
                error.config.headers.Authorization =
                    'JWT ' + store.state.authUser.accessToken
                
                await axios.request(error.config)

            } catch (e) {
                console.log('e')
                if (axios.isAxiosError(e)) {
                    console.log('axios error')
                    if (e.request.status == 401) {
                        console.log('強制ログアウト')
                        store.dispatch('authLogout')
                    }
                }
            }
        }
        isRetry = false
        return Promise.reject(error)
    }
)

export default axios.create({
    baseURL: 'https://127.0.0.1:8000/api/v1'
})
