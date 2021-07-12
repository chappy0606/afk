import { createStore, Store, useStore as baseUseStore } from 'vuex'
import { InjectionKey } from 'vue'
import { Token } from './modules/Token'

export interface ChapterStageList {
    chapters: string
    stages: string
}
export interface State {
    token: Token
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
    state: {
        token: {
            accsesToken: '',
            refreshToken: ''
        }
    }
})

export const useStore = (): Store<State> => {
    return baseUseStore(key)
}
