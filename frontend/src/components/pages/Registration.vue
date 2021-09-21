<template>
    <div>
        <div class="input-form">
            <label>ユーザー名</label><br>
                <input type="text" v-model="userName" />
                    <label v-if="errorMessages.username">
                        {{errorMessages.username}}
                    </label>
                    <label v-else>最低１文字必要です。</label><br>

            <label>パスワード</label><br>
                <input type="password" v-model="passWord" />
                    <label v-if="errorMessages.password">
                        {{errorMessages.password}}
                    </label>
                    <label v-else>大小英字、数字を含む8文字以上必要です</label><br>
                <input type="checkbox" />
                    <label>パスワードの表示</label><br>

            <label>メールアドレス</label><br>
                <input type="text" v-model="eMail" />
                    <label v-if="errorMessages.email">
                        {{errorMessages.email}}
                    </label>
                    <label v-else>パスワード再発行時に使用します(任意)</label><br>

            <button @click="userRegister">Sign up</button>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent, ref, reactive } from 'vue'
import { useRouter } from 'vue-router'

interface response {
    username: string
    password: string
    email: string
}
export default defineComponent({
    setup() {
        const router = useRouter()

        const userName = ref<string>('')
        const passWord = ref<string>('')
        const eMail = ref<string>('')

        const errorMessages: response = reactive({
            username: '',
            password: '',
            email: ''
        })

        const isShowPassword = () => {
            console.log('')
        }

        const userRegister = () => {
            axios
                .post('https://127.0.0.1:8000/api/v1/auth/registration/', {
                    username: userName.value,
                    password: passWord.value,
                    email: eMail.value
                })
                .then(respnse => {
                    console.log(respnse)
                    router.push({
                        name: 'PveComp'
                    })
                })
                .catch(error => {
                    for(const key in error.response.data){
                        if(key in errorMessages){
                            errorMessages[key] = error.response.data[key][0]
                        }
                    }
                })
        }

        return {
            userName,
            passWord,
            eMail,
            errorMessages,
            userRegister
        }
    }
})
</script>
