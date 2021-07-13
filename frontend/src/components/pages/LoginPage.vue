<template>
    <div>
        <input v-model="userName" type="text" placeholder="ユーザー名" />
        <input
            v-model="passWord"
            type="text"
            placeholder="ログインパスワード"
        />
        <button @click="login">ログイン</button>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import{ useStore } from '../../store'
import axios from 'axios'

export default defineComponent({
    setup() {

        const store = useStore()
        console.log(store.state.counter)
        
        const userName = ref<string>('master')
        const passWord = ref<string>('chappy0606')
        let user = ref<string>()
        
        const login = (): void => {
    
            axios
                .post('https://localhost:8000/api/v1/auth/jwt/create', {
                    username: userName.value,
                    password: passWord.value
                })
                .then(response => {
                    const accessToken: string = response.data.access
                    const refreshToken: string = response.data.refresh
                    store.commit('setToken', {accessToken, refreshToken})
                    console.log(store.state.token)
                    axios
                        .get('https://localhost:8000/api/v1/account/user/', {
                            headers: {
                                Authorization: 'JWT ' + accessToken
                            }
                        })
                        .then(response => {
                            user.value = response.data
                        })
                })
        }

        return {
            login,
            userName,
            passWord,
            user,
            store
        }
    }
})
</script>