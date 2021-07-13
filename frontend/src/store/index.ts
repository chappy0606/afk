import { createStore, Store, useStore as baseUseStore } from 'vuex'
import { InjectionKey } from 'vue'
import { Token } from './modules/Token'
import { ChapterStageList } from './modules/ChapterStage'

interface State {
    token: Token
    chpaterStage: ChapterStageList
    counter: number
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
    state: {
        token: {
            accessToken: '',
            refreshToken: ''
        },
        chpaterStage: {
            chapters: '',
            stages: ''
        },
        counter: 0
    },
    mutations: {
        setToken(state, token: Token) {
            state.token.accessToken = token.accessToken
            state.token.refreshToken = token.refreshToken
        },
        test(counter){
            counter.counter = counter.counter + 1
        }
    }
})

export const useStore = (): Store<State> => {
    return baseUseStore(key)
}
