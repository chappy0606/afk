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
        const userName = ref<string>('')
        const passWord = ref<string>('')

        const login = (): void => {
            console.log(userName.value)
            console.log(passWord.value)
            axios
                .post('http://127.0.0.1:8000/api/v1/token/', {
                    username: userName.value,
                    password: passWord.value
                })
                .then(response => console.log(response.data))
        }
        return {
            login,
            userName,
            passWord
        }
    }
})
</script>
