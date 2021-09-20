<template>
    <div>
        <input type="text" v-model="userName" placeholder="ユーザー名" />
        <input type="password" v-model="passWord" placeholder="パスワード" />
        <input type="text" v-model="eMail" placeholder="メールアドレス(任意)" />
        <button @click="userRegister">登録</button>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent, ref } from 'vue'
export default defineComponent({
    setup() {
        const userName = ref<string>('')
        const passWord = ref<string>('')
        // todo: 間違って空白入ったときは空白チェックでお茶濁す
        const eMail = ref<string>('')

        const userRegister = () => {
            axios
                .post('https://127.0.0.1:8000/api/v1/auth/registration/', {
                    username: userName.value,
                    password: passWord.value,
                    email: eMail.value
                })
                .then(respnse => {
                    console.log(respnse)
                })
                .catch(error => {
                    console.log(error.response)
                })
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
