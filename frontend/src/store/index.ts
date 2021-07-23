import { createStore, Store, useStore as baseUseStore } from 'vuex'
import { InjectionKey } from 'vue'
import { User, Auth, Path } from './modules/Types'
import axios from 'axios'
import router from '@/router'

interface State {
    authUser: User
    auth: Auth
    path: Path
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
                    commit('setAuthUser', response.data)
                    commit('isAuth', true)
                    if (store.state.path.currentPath) {
                        router.push({ path: store.state.path.currentPath })
                    } else {
                        router.push({path:'/'})
                    }
                })
                .catch(error => {
                    console.log(error.response)
                    commit('isAuth', false)
                })
        }
    }
})

export const useStore = (): Store<State> => {
    return baseUseStore(key)
}
