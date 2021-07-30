<template>
    <header>
        <span v-if="store.state.auth.isAuth">
            {{ store.state.authUser.user.username }}さん
        </span>
        <nav class="header-menu">
            <ul>
                <li><router-link to="/login">ログイン</router-link></li>
                <router-link to="/">トップページ</router-link>
                <li><a href="#">ユーザー登録</a></li>
            </ul>
            <button @click="logout">ログアウト</button>
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
            store.dispatch('authLogout')
        }

        return {
            store,
            logout
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
