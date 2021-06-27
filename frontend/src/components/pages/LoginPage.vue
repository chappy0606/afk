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
                .post('http://127.0.0.1:8000/api/v1/auth/jwt/create', {
                    username: userName.value,
                    password: passWord.value
                })
                .then(r => {
                    console.log((jwtToken = r.data.access))
                    axios
                        .get('http://127.0.0.1:8000/api/v1/account/user/', {
                            headers: {
                                Authorization: 'JWT ' + jwtToken
                            }
                        })
                        .then(r => console.log(r.data))
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

// curl \ // -X POST \ // -H "Content-Type: application/json" \ // -d
'{"username": "master", "password": "chappy0606"}' \ //
http://localhost:8000/api/v1/token/