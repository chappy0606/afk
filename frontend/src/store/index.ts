import { createStore, Store, useStore as baseUseStore } from 'vuex'
import { InjectionKey } from 'vue'
import { User, Auth, Path } from './modules/Types'
import axios from '../export'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'
import Cookies from 'js-cookie'

interface State {
    authUser: User
    auth: Auth
    path: Path
}

const initializeState = (): User => {
    return {
        user: {
            id: null,
            userName: ''
        },
        accessToken: '',
        refreshToken: ''
    }
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
    state: {
        authUser: {
            user: {
                id: null,
                userName: '',
            },
            accessToken: '',
            refreshToken: ''
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
                'authUser.user.userName',
                'auth.isAuth',
                'authUser.accessToken',
                'authUser.refreshToken'
            ]
        })
    ],

    mutations: {
        setAuthUser: (state, user: User): void => {
            state.authUser = user
        },

        setAccessToken: (state, accsseToken: string): void => {
            state.authUser.accessToken = accsseToken
        },

        isAuth: (state, auth): void => {
            state.auth.isAuth = auth
        },

        setCurrentPath: (state, path: Path): void => {
            state.path.currentPath = path.currentPath
        }
    },

    actions: {
        authLogin: ({ commit, state }, payload: string): void => {
            axios
                .post('/auth/login/', payload)
                .then(response => {
                    commit('setAuthUser', response.data)
                    commit('isAuth', true)
                    if (state.path.currentPath) {
                        router.push({
                            path: state.path.currentPath
                        })
                        } else{
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
                .post('/auth/logout/')
                .then( () => {
                    commit('isAuth', null)
                    commit('setAuthUser', initializeState())
                    commit('setCurrentPath', '')
                    router.push({name: 'TopPage'})
                })
        }
    }
})

export const useStore = (): Store<State> => {
    return baseUseStore(key)
}