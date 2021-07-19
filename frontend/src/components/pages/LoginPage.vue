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
import { useStore } from '../../store'
import axios from 'axios'

export default defineComponent({
    setup() {
        const store = useStore()

        const userName = ref<string>('master')
        const passWord = ref<string>('chappy0606')

        const login = (): void => {
            store.dispatch('authLogin',{userName,passWord})
            // axios
            //     .post('https://127.0.0.1:8000/api/v1/auth/login/', {
            //         username: userName.value,
            //         password: passWord.value
            //     })
            //     .then(response => {
            //         const user = response.data
            //         store.commit('setAuthUser',user)
            //     })
        }

        return {
            login,
            userName,
            passWord,
        }
    }
})
</script>
