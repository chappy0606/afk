<template>
    <div>
        <div class="input-form">
            <div class="username">
                <input type="text" v-model="userName" placeholder="ユーザー名" />
                    <span v-if="errorMessages.username">
                        {{errorMessages.username}}
                    </span>
            </div>

            <div class="password">
                <input type="password" v-model="passWord" placeholder="パスワード"/>
                    <span v-if="errorMessages.password">
                        {{errorMessages.password}}
                    </span>
            </div>

        <div class="email">
            <input type="text" v-model="eMail" placeholder="メールアドレス(任意)"/>
                <span v-if="errorMessages.email">
                    {{errorMessages.email}}
                </span>
        </div>
        
        <button @click="userRegister">登録</button>
        
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
