<template>
    <div>
        <form>
        <input v-model="userName" type="text">
        <input v-model="passWord" type="text">
        <button @click="login" type="submit">ログイン</button>
        </form>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from 'axios'

export default defineComponent({
    setup() {
        const userName = Stringf
        let passWord: string = ''

        const login =  (event: {target: HTMLButtonElement}): void => {
            console.log('呼ばれてますか？')
            console.log(event.target.value)
            // axios.post('http://127.0.0.1:8000/api/v1/rest-auth/login/',)
        }
        return{
            login,
            userName,
            passWord
        }
    },

})
</script>
