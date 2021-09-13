<template>
    <div>
        <input type="text" v-model="userName" placeholder="ユーザー名" />
        <input type="password" v-model="passWord" placeholder="パスワード" />
        <input type="text" v-model="eMail" placeholder="メールアドレス(任意)" />
        <button @click="userRegister">登録</button>
    </div>
</template>

<script lang="ts">
import { defineComponent,ref } from 'vue'
export default defineComponent({
    setup() {


        const userName = ref<string>('')
        const passWord = ref<string>('')
        const eMail = ref<string>('')

        const userRegister =() =>{
            console.log(userName)
            console.log(passWord)
            console.log(eMail)
        }

        return {
            userName,
            passWord,
            eMail,
            userRegister
        }
    }
})
</script>
