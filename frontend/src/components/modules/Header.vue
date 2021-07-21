<template>
    <header>
        <span v-if="store.state.authUser.user.username">
            {{ store.state.authUser.user.username }}さん
        </span>
        <nav class="header-menu">
            <ul>
                <form name="logout" method="POST" action="#">
                    <li><a href="javascript:logout.submit()">ログアウト</a></li>
                </form>
                <li><router-link to="/login">ログイン</router-link></li>
                <router-link to="/">トップページ</router-link>
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

        return {
            store
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
