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
import { defineComponent} from 'vue'
import { useStore } from '../../store'

export default defineComponent({
    setup() {
        const store = useStore()

        const userName = 'master'
        const passWord = 'chappy0606'

        const login = (): void => {
            store.dispatch('authLogin', { username: userName, password: passWord })
        }

        return {
            login,
            userName,
            passWord,
        }
    }
})
</script>
