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
