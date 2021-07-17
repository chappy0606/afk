<template>
    <header>
        <template v-for="user in store.state.user">
            <span v-if="user.username" :key="user">
                {{ user.username }}さん
            </span>
        </template>
        <nav class="header-menu">
            <ul>
                <form name="logout" method="POST" action="#">
                    <li><a href="javascript:logout.submit()">ログアウト</a></li>
                </form>
                <router-link to="/login">ログイン</router-link>
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
