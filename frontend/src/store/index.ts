import { createStore, Store, useStore as baseUseStore } from 'vuex'
import { InjectionKey } from 'vue'
import { User } from './modules/User'

interface State {
    user: User
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
    state: {
        user: {
            id: null,
            username: '',
            password: '',
            email: '',
            is_staff: false,
            is_active: true,
            date_joined: '',
            token: {
                accessToken: '',
                refreshToken: ''
            }
        }
    },
    mutations: {
        setAuthUser(state, user) {
            state.user = user
        }
    }
})

export const useStore = (): Store<State> => {
    return baseUseStore(key)
}
