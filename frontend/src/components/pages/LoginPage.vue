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

        const login = (): void => {
            let jwtToken: string

            axios
                .post('http://127.0.0.1:8000/api/v1/token/', {
                    username: userName.value,
                    password: passWord.value
                })
                .then(response => {
                    jwtToken = response.data.token
                })
            axios
                .post('http://127.0.0.1:8000/api/v1/rest-auth/login/', {
                    username: userName.value,
                    password: passWord.value,
                    headers: {
                        Authorization: 'JWT ' + jwtToken
                    }
                })
                .then(response => {
                    console.log(response.data)
                })
        }
        return {
            login,
            userName,
            passWord
        }
    }
})
</script>
