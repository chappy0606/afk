<template>
    <div>
        <input type="text" placeholder="ユーザー名" />
        <input type="password" placeholder="パスワード" />
        <input type="text" placeholder="メールアドレス(任意)" />
        <button @click="userRegister">登録</button>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    setup() {

        return {
        }
    }
})
</script>
