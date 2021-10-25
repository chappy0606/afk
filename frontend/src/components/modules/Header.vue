<template>
    <header>
        <span v-if="store.state.auth.isAuth">
            <router-link :to="{ name: 'Profile'}">
                <h3>{{ store.state.authUser.user.userName}}さん</h3>
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
    </header>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import { useStore } from '../../store'
export default defineComponent({
    setup() {
        const store = useStore()

        const logout = (): void => {
            if (confirm('本当にログアウトしますか？')) {
                store.dispatch('authLogout')
            }
        }

        return {
            store,
            logout,
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