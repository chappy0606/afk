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
            axios
                .post('https://localhost:8000/api/v1/auth/jwt/create', {
                    username: userName.value,
                    password: passWord.value
                })
                .then(response => {
                    const accessToken = response.data.access
                    const refreshToken = response.data.refresh
                    axios
                        .get(
                            'https://localhost:8000/api/v1/account/user/',
                            {
                                headers: {
                                    Authorization: 'JWT ' + accessToken
                                }
                            }
                        )
                        .then(response => {
                            const user = response.data[0]
                            user.token = {accessToken, refreshToken}
                            store.commit('setAuthUser',
                                user
                            )
                        })
                })
        }

        return {
            login,
            userName,
            passWord,
        }
    }
})
</script>
