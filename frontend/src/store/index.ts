import { createStore, Store, useStore as baseUseStore } from 'vuex'
import { InjectionKey } from 'vue'


export interface token {
    accsesToken: string
    refreshToken: string
    counter: number
}

export const key: InjectionKey<Store<token>> = Symbol()

export const store = createStore<token>({
    state: {
        accsesToken: '',
        refreshToken: '',
        counter: 0
    }
})

export const useStore = (): Store<token> => {
    return baseUseStore(key)
}