<template>
    <header>
        <span v-if="store.state.auth.isAuth">
            <router-link :to="{ name: 'Profile'}">
                <h3>{{ store.state.authUser.user.username }}さん</h3>
            </router-link>
        </span>

        <nav class="header-menu">
            <ul>
                <button v-show="store.state.auth.isAuth" @click="logout">ログアウト</button>
                <li v-show="!store.state.auth.isAuth"><router-link :to="{ name: 'Login' }">ログイン</router-link></li>
                <li><router-link :to="{ name: 'TopPage' }">トップページ</router-link></li>
                <li v-show="!store.state.auth.isAuth"><router-link :to="{ name: 'Registration' }">ユーザー登録</router-link></li>
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
            axios
                .delete('https://127.0.0.1:8000/api/v1/auth/user/',{
                    headers: {
                        Authorization:
                            'JWT ' + store.state.authUser.access_token
                    }
                })
                .then(response => {
                    console.log(response.request.response)
                })
                .catch(error => {
                    console.log(error)
                })
        }

        return {
            store,
            logout,
            test,
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