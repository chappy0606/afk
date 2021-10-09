<template>
    <div>
        <div class="input-form">
            <label>ユーザー名</label><br>
                <input id="username" type="text" v-model="req.userName" />
                    <label v-if="resp.userName">{{resp.userName}}</label>
                    <label v-else>最低１文字必要です。</label><br>

            <label>パスワード</label><br>
                <input id="password" type="password" v-model="req.password" />
                <span id="buttonEye" class="fa fa-eye" @click="showPassword"></span>
                    <label v-if="resp.password">{{resp.password}}</label>
                    <label v-else>大小英字、数字を含む8文字以上必要です</label><br>

            <label>メールアドレス</label><br>
                <input id="email" type="text" v-model="req.email" />
                    <label v-if="resp.email">{{resp.email}}</label>
                    <label v-else>パスワード再発行時に使用します(任意)</label><br>

            <button @click="userRegister">Sign up</button>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from '../../store'

interface RequestData {
    userName: string
    password: string
    email: string
}

interface ResponseData {
    userName: string
    password: string
    email: string
}

export default defineComponent({
    setup() {
        const router = useRouter()
        const store = useStore()

        const req: RequestData = reactive({
            userName: '',
            password: '',
            email: ''
        })

        const resp: ResponseData = reactive({
            userName: '',
            password: '',
            email: ''
        })

        const showPassword = () => {
            const inputType = document.getElementById('password') as HTMLElement
            const className = document.getElementById('buttonEye') as HTMLElement

            if (inputType.getAttribute('type') === 'password'){
                inputType.setAttribute('type','text')
                className.setAttribute('class','fa fa-eye-slash')
            }
            else{
                inputType.setAttribute('type','password')
                className.setAttribute('class','fa fa-eye')
            }
        }

        const userRegister = () => {
            axios
                .post('https://127.0.0.1:8000/api/v1/auth/registration/', {
                    userName: req.userName,
                    password: req.password,
                    email: req.email
                })
                .then(respnse => {
                    console.log(respnse)
                    store.dispatch('authLogin',{userName:req.userName, password:req.password})
                    router.push({
                        name: 'TopPage'
                    })
                })
                .catch(error => {
                    for (const key in error.response.data){
                        resp[key as keyof ResponseData] = error.response.data[key][0]
                    }
                })
        }

        return {
            req,
            resp,
            userRegister,
            showPassword
        }
    }
})
</script>