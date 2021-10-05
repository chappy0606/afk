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
import { useStore } from '../../store'

export default defineComponent({
    setup() {

        const store = useStore()
        
        const userName = ref<string>('todo')
        const passWord = ref<string>('Chappy0606')

        const login = (): void => {
            store.dispatch('authLogin', { user_name: userName.value, password: passWord.value })
        }

        return {
            login,
            userName,
            passWord,
        }
    }
})
</script>