import { createStore, Store, useStore as baseUseStore } from 'vuex'
import { InjectionKey } from 'vue'
import { User, Auth } from './modules/User'
import axios from 'axios'

interface State {
    authUser: User
    auth: Auth
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
        }
    },

    mutations: {
        setAuthUser: (state, user: User): void => {
            state.authUser = user
        },
        isAuth: (state, auth): void => {
            state.auth.isAuth = auth
        }
    },

    actions: {
        authLogin: ({ commit }, payload: string): void => {
            axios
                .post('https://127.0.0.1:8000/api/v1/auth/login/', payload)
                .then(response => {
                    commit('setAuthUser', response.data)
                    commit('isAuth', true)
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
