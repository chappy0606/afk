<template>
    <div>
        <div class="input-form">
            <label>ユーザー名</label><br>
                <input id="username" type="text" v-model="userName" />
                    <label v-if="errorMessages.username">{{errorMessages.username}}</label>
                    <label v-else>最低１文字必要です。</label><br>

            <label>パスワード</label><br>
                <input id="password" type="password" v-model="passWord" />
                    <label v-if="errorMessages.password">{{errorMessages.password}}</label>
                    <label v-else>大小英字、数字を含む8文字以上必要です</label><br>
                    <label><input type="checkbox" @change="showPassword" />パスワードの表示</label><br>

            <label>メールアドレス</label><br>
                <input id="email" type="text" v-model="eMail" />
                    <label v-if="errorMessages.email">{{errorMessages.email}}</label>
                    <label v-else>パスワードリセット時に使用します(任意)</label><br>

            <button @click="userRegister">Sign up</button>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent, ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from '../../store'

interface response {
    username: string
    password: string
    email: string
}
export default defineComponent({
    setup() {
        const router = useRouter()
        const store = useStore()

        const userName = ref<string>('')
        const passWord = ref<string>('')
        const eMail = ref<string>('')

        const errorMessages: response = reactive({
            username: '',
            password: '',
            email: ''
        })

        const showPassword = () => {
            const elm = document.getElementById('password')
            if (elm.getAttribute('type') === 'password'){
                elm.setAttribute('type','text')
            }else{
                elm.setAttribute('type','password')
            }
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
                    store.dispatch('authLogin',{username:userName.value, password:passWord.value})
                    router.push({
                        name: 'TopPage'
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
            userRegister,
            showPassword
        }
    }
})
</script>
