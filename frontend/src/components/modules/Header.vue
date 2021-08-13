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
            store.dispatch('authLogout')
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
                .then(res => {
                    console.log('認証成功！')
                    console.log(res.request)
                })
                .catch(error => {
                    console.log('認証失敗！')
                    console.log('トークンが有効か確認するよ')
                    if (error.response.status === 401) {
                        axios
                            .post(
                                'https://127.0.0.1:8000/api/v1/auth/token/verify/',
                                {'token':store.state.authUser.refresh_token},
                            )
                            .then(response => {
                                // 空の時true(refreshtoken生きてる)
                                if(!Object.keys(response.data).length){
                                    console.log('true')
                                }else{
                                    console.log('false')
                                }
                            })
                            .catch(error => {
                                console.log(error.response)
                            })
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
