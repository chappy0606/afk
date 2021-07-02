<template>
    <header>
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
import {defineComponent} from 'vue'
export default defineComponent({
    
})
</script>
<style>
header {
    font-size: 20px;
    width: 100%;
}
</style>
