import { createStore, Store, useStore as baseUseStore } from 'vuex'
import { InjectionKey } from 'vue'
import { User, Auth, Path } from './modules/Types'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'
import Cookies from 'js-cookie'

interface State {
    authUser: User
    auth: Auth
    path: Path
}

const initialState = (): User => {
    return {
        user: {
            id: null,
            is_active: null,
            is_staff: null,
            password: '',
            username: '',
            last_login: '',
            date_joined: '',
            email: ''
        },
        access_token: '',
        refresh_token: ''
    }
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
    state: {
        authUser: {
            user: {
                id: null,
                is_active: null,
                is_staff: null,
                password: '',
                username: '',
                last_login: '',
                date_joined: '',
                email: ''
            },
            access_token: '',
            refresh_token: ''
        },

        auth: {
            isAuth: null
        },
        path: {
            currentPath: ''
        }
    },
    plugins: [
        createPersistedState({
            key: 'testKey',
            storage: {
                getItem: key => Cookies.get(key),
                setItem: (key, value) =>
                    Cookies.set(key, value, {
                        expires: 7,
                        secure: true
                    }),
                removeItem: key => Cookies.remove(key)
            },
            paths: [
                'authUser.user.id',
                'authUser.user.username',
                'auth.isAuth',
                'authUser.access_token',
                'authUser.refresh_token'
            ]
        })
    ],

    mutations: {
        setAuthUser: (state, user: User): void => {
            state.authUser = user
        },

        setAccessToken: (state, accsseToken: string): void => {
            state.authUser.access_token = accsseToken
        },

        isAuth: (state, auth): void => {
            state.auth.isAuth = auth
        },

        setCurrentPath: (state, path: Path): void => {
            state.path.currentPath = path.currentPath
        }
    },

    actions: {
        accessTokenRefresh: ({ commit, state }) => {
            axios
                .post(
                    'https://127.0.0.1:8000/api/v1/auth/token/refresh/',
                    {
                        refresh: state.authUser.refresh_token
                    }
                )
                .then(response => {
                    console.log('更新完了！')
                    console.log('認証成功やで！！！')
                    commit('setAccessToken', response.data.access)
                })
                .catch(error => {
                    if (error.response.status === 401) {
                        store.dispatch('authLogout')
                    } else {
                        console.log(error.response)
                    }
                }
            )
        },

        authLogin: ({ commit, state }, payload: string): void => {
            axios
                .post('https://127.0.0.1:8000/api/v1/auth/login/', payload)
                .then(response => {
                    commit('setAuthUser', response.data)
                    commit('isAuth', true)
                    if (state.path.currentPath) {
                        console.log('pathあるで！')
                        router.push({
                            path: state.path.currentPath
                        })
                        } else if (!state.path.currentPath) {
                                router.push({ name: 'TopPage' })
                        }
                })
                .catch(error => {
                    console.log(error.response)
                    commit('isAuth', false)
                })
        },
        authLogout: ({ commit }) => {
            axios
                .post('https://127.0.0.1:8000/api/v1/auth/logout/')
                .then( () => {
                    console.log('ログアウトしました')
                    commit('isAuth', null)
                    commit('setAuthUser', initialState())
                    commit('setCurrentPath', '')
                    router.push({name: 'TopPage'})
                })
        }
    }
})

export const useStore = (): Store<State> => {
    return baseUseStore(key)
}