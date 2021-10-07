<template>
    <div>
        <h2>パスワードの変更</h2>
        <label>変更前のパスワード</label><br />
        <input
            id="old-password"
            type="text"
            v-model="req.oldPassword"
            @change="getPassWord"
        />
        <br />
        <label>変更後のパスワード</label><br />
        <input
            id="new-password"
            type="text"
            v-model="req.newPassword"
            @change="getPassWord"
        />
        <button @click="passwordUpdate">更新</button>
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

        const passwordUpdate = () => {
            console.log(req.newPassword)
            console.log(store.state.authUser.accessToken)
            axios.post(
                'https://127.0.0.1:8000/api/v1/auth/password/change/',
                {
                    oldPassword: req.oldPassword,
                    newPassword1: req.newPassword,
                    newPassword2: req.newPassword
                },
                {
                    headers: {
                        Authorization:
                            'JWT ' + store.state.authUser.accessToken
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
            passwordUpdate
        }
    }
})
</script>
