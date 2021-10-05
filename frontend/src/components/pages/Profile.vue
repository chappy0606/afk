<template>
    <div>
        <h2>パスワードの変更</h2>
        <label>変更前のパスワード</label><br />
        <input
            id="old-password"
            type="text"
            v-model="req.oldPassWord"
            @change="getPassWord"
        />
        <br />
        <label>変更後のパスワード</label><br />
        <input
            id="new-password"
            type="text"
            v-model="req.newPassWord"
            @change="getPassWord"
        />
        <button @click="passWordUpdate">更新</button>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent, reactive } from 'vue'
import { useStore } from '../../store'


interface RequestData {
    newPassword: string
    oldPassword: string
}

interface ResponseData {
    newPassword: string
    oldPassword: string
    success: string
}

export default defineComponent({
    setup() {
        const req: RequestData = reactive({
            newPassword: '',
            oldPassword: ''
        })

        const resp : ResponseData = reactive({
            newPassword: '',
            oldPassword: '',
            success: ''
        })


        const store = useStore()

        const getPassWord = (event: { target: HTMLInputElement }) => {
            if (event.target.id === 'old-password') {
                req.oldPassword = event.target.value
            } else if (event.target.id === 'new-password') {
                req.newPassword = event.target.value
            }
        }

        const passWordUpdate = () => {
            axios.post(
                'https://127.0.0.1:8000/api/v1/auth/password/change/',
                {
                    old_password: req.oldPassword,
                    new_password1: req.newPassword,
                    new_password2: req.newPassword
                },
                {
                    headers: {
                        Authorization:
                            'JWT ' + store.state.authUser.access_token
                    }
                }
            )
            .then(() => {
                resp.success = 'パスワードの更新が完了しました。'
            })
            .catch(error => {
                console.log(error)
            })
        }

        return {
            req,
            getPassWord,
            passWordUpdate
        }
    }
})
</script>
