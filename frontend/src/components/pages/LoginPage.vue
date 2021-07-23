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
import { defineComponent, ref} from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from '../../store'

export default defineComponent({
    setup() {
        const store = useStore()

        const userName = ref('master')
        const passWord = ref('chappy0606')

        const login = (): void => {
            store.dispatch('authLogin', { username: userName.value, password: passWord.value })
        }

        return {
            login,
            userName,
            passWord,
        }
    }
})
</script>
