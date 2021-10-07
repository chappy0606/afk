<template>
    <div>
        <input v-model="userName" type="text" placeholder="ユーザー名" />
        <input
            v-model="password"
            type="text"
            placeholder="ログインパスワード"
        />
        <button @click="login">ログイン</button>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref} from 'vue'
import { useStore } from '../../store'

export default defineComponent({
    setup() {

        const store = useStore()
        
        const userName = ref<string>('todo')
        const password = ref<string>('Chappy0606')

        const login = (): void => {
            store.dispatch('authLogin', { userName: userName.value, password: password.value })
        }

        return {
            login,
            userName,
            password,
        }
    }
})
</script>