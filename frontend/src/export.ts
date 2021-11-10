import axios, { AxiosResponse } from 'axios'
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

                store.commit('setAccessToken', response.data.access)
                error.config.headers.Authorization =
                    'JWT ' + store.state.authUser.accessToken
                
                return await axios.request(error.config)

            } catch (e) {
                if (axios.isAxiosError(e)) {
                    if (e.request.status == 401) {
                        // refreshToken期限切れで強制ログアウト
                        store.dispatch('authLogout')
                    }
                }
            }
        }
        return Promise.reject(error)
    }
)

export default axios
