<template>
    <div>
        <input type="text" placeholder="ユーザー名" />
        <input type="password" placeholder="パスワード" />
        <input type="text" placeholder="メールアドレス(任意)" />
        <button @click="userRegister">登録</button>
    </div>
</template>

<script lang="ts">
// import axios from 'axios'
import { defineComponent } from 'vue'
export default defineComponent({
    setup() {
        const userRegister = () => {
            console.log('登録ーーーーーーーーーーーーーーーー')
        }

        return {
            userRegister
        }
    }
})
</script>
