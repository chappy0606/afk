import { createStore, Store, useStore as baseUseStore } from 'vuex'
import { InjectionKey } from 'vue'
import { User, AuthUser } from './modules/User'
import axios from 'axios'

interface State {
    user: User
    authUser: AuthUser
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
    state: {
        authUser: {
            authUser: null
        },
        user: {
            userInfo: {
                id: null,
                username: '',
                password: '',
                email: '',
                is_staff: false,
                is_active: true,
                date_joined: ''
            },
            accessToken: '',
            refreshToken: ''
        }
    },
    mutations: {
        setAuthUser: (state, authUser) => {
            state.user = authUser
        }
    },
    actions: {
        authLogin: (store, user) => {
            axios
                .post('https://127.0.0.1:8000/api/v1/auth/login/', {
                    username: user.userName.value,
                    password: user.passWord.value
                })
                .then(response => {
                    store.commit('setAuthUser', response.data)
                })
        }
    }
})

export const useStore = (): Store<State> => {
    return baseUseStore(key)
}
