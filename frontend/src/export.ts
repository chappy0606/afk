import axios from 'axios'
import { useStore } from './store'

const store = useStore()

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
                    store.commit('setAccessToken', response.data.access)
                })
                .catch(error => {
                    if (error.response.status === 401) {
                        // refreshToken期限切れで強制ログアウト
                        store.dispatch('authLogout')
                    } else {
                        console.log(error.response)
                    }
                })
        }
    }
)

export default axios
