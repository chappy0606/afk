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
                'authUser.user.username',
                'auth.isAuth',
                'authUser.access_token',
                'authUser.refresh_token',
            ]
        })
    ],

    mutations: {
        setAuthUser: (state, user: User): void => {
            state.authUser = user
        },

        isAuth: (state, auth): void => {
            state.auth.isAuth = auth
        },

        setCurrentPath: (state, path: Path): void => {
            state.path.currentPath = path.currentPath
        }
    },

    actions: {
        authLogin: ({ commit }, payload: string): void => {
            axios
                .post('https://127.0.0.1:8000/api/v1/auth/login/', payload)
                .then(response => {
                    console.log(response.data)
                    commit('setAuthUser', response.data)
                    commit('isAuth', true)
                    if (store.state.path.currentPath) {
                        router.push({
                            path: store.state.path.currentPath
                        })
                    } else {
                        router.push({ path: '/' })
                    }
                })
                .catch(error => {
                    console.log(error.response)
                    commit('isAuth', false)
                })
        },
        authLogout: ({ commit }) => {
            if (confirm('本当にログアウトしますか？')) {
                axios
                    .post('https://127.0.0.1:8000/api/v1/auth/logout/')
                    .then(response => {
                        console.log(response.data.detail)
                        commit('isAuth', null)
                        commit('setAuthUser', initialState())
                        router.push('/')
                    })
            }
        }
    }
})

export const useStore = (): Store<State> => {
    return baseUseStore(key)
}
