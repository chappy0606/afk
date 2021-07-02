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
import axios from 'axios'

export default defineComponent({
    setup() {

        const userName = ref<string>('master')
        const passWord = ref<string>('chappy0606')
        let user = ref<string>()
        
        const login = (): void => {
            let jwtToken: string

            axios
                .post('https://localhost:8000/api/v1/auth/jwt/create', {
                    username: userName.value,
                    password: passWord.value
                })
                .then(response => {
                    console.log((jwtToken = response.data.access))
                    axios
                        .get('https://localhost:8000/api/v1/account/user/', {
                            headers: {
                                Authorization: 'JWT ' + jwtToken
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
            user
        }
    }
})
</script>