<template>
    <header>
        <span v-if="store.state.auth.isAuth">
            {{ store.state.authUser.user.username }}さん
        </span>
        <nav class="header-menu">
            <ul>
                <button v-if="store.state.auth.isAuth" @click="logout">
                    ログアウト
                </button>
                <li v-else><router-link to="/login">ログイン</router-link></li>
                <li><router-link to="/">トップページ</router-link></li>
                <li><a href="#">ユーザー登録</a></li>
            </ul>
        </nav>
        <button @click="test">認証テスト</button>
    </header>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import { useStore } from '../../store'
import axios from 'axios'
export default defineComponent({
    setup() {
        const store = useStore()

        const logout = (): void => {
            if (confirm('本当にログアウトしますか？')) {
                store.dispatch('authLogout')
            }
        }

        const test = (): void => {
            // 認証チェック
            axios
                .get('https://127.0.0.1:8000/api/v1/test/', {
                    headers: {
                        Authorization:
                            'JWT ' + store.state.authUser.access_token
                    }
                })
                .then(response => {
                    console.log('認証成功！')
                    console.log(response.request.response)
                })
                .catch(error => {
                    if (error.response.status === 401) {
                        console.log('アクセストークン更新できるか確認するわ！')
                        store.dispatch('accessTokenRefresh')
                    }
                })
        }

        return {
            store,
            logout,
            test
        }
    }
})
</script>
<style>
header {
    font-size: 20px;
    width: 100%;
}
</style>