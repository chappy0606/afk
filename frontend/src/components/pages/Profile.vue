<template>
    <div>
        <h2>パスワードの変更</h2>
        <label>変更前のパスワード</label><br />
        <input
            id="old-password"
            type="text"
            v-model="inputData.oldPassWord"
            @change="test"
        />
        <br />
        <label>変更後のパスワード</label><br />
        <input
            id="new-password"
            type="text"
            v-model="inputData.newPassWord"
            @change="test"
        />
        <button @click="passWordUpdate">更新</button>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent, reactive } from 'vue'
import { useStore } from '../../store'

interface PassWord {
    newPassWord: string
    oldPassWord: string
}

interface Message extends PassWord{
    success: string
}

export default defineComponent({
    setup() {
        const inputData: PassWord = reactive({
            newPassWord: '',
            oldPassWord: ''
        })

        const message : Message = reactive({
            newPassWord: '',
            oldPassWord: '',
            success: ''
        })

        const store = useStore()

        const test = (event: { target: HTMLInputElement }) => {
            if (event.target.id === 'old-password') {
                inputData.oldPassWord = event.target.value
            } else if (event.target.id === 'new-password') {
                inputData.newPassWord = event.target.value
            }
        }

        const passWordUpdate = () => {
            axios.post(
                'https://127.0.0.1:8000/api/v1/auth/password/change/',
                {
                    old_password: inputData.oldPassWord,
                    new_password1: inputData.newPassWord,
                    new_password2: inputData.newPassWord
                },
                {
                    headers: {
                        Authorization:
                            'JWT ' + store.state.authUser.access_token
                    }
                }
            )
            .then(() => {
                message.success = 'パスワードの更新が完了しました。'
            })
            .catch( (error) => {
                console.log(error)
            })
        }

        return {
            inputData,
            test,
            passWordUpdate
        }
    }
})
</script>
