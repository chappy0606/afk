<template>
    <div id="app">
        <Header />
        <router-view class="active-component" />
        <Footer />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Header from './components/modules/Header.vue'
import Footer from './components/modules/Footer.vue'
import axios from './export'
import { useStore } from './store'

export default defineComponent({
    components: { Header, Footer },
    setup() {
        const store = useStore()

        if (store.state.auth.isAuth) {
            axios
                .post('/auth/token/verify/', {
                    token: store.state.authUser.refreshToken
                })
                .catch(() => {
                    store.dispatch('authLogout')
                })
        }
    }
})
</script>

<style>
/* スタイルのリセット */
* {
    margin: 0;
    padding: 0;
}

html,
body {
    height: 100%;
    background-color: rgb(82, 82, 82);
}

#app {
    height: 100%;
    display: flex;
    flex-direction: column;
    font-family: 'ヒラギノ角ゴ Pro W3', 'Hiragino Kaku Gothic Pro', 'メイリオ',
        Meiryo, Osaka, 'MSPゴシック', 'MS PGothic', sans-serif;
    -webkit-text-size-adjust: none;
    width: 100%;
}

.active-component {
    flex: 1;
}

</style>
