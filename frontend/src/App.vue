<template>
    <div id="app">
        <Header />
        <router-view />
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
* {
    margin: 0px;
    padding: 0px;
}
html,
body {
    height: 100%;
}

body {
    background-color: rgb(82, 82, 82);
    font-family: 'ヒラギノ角ゴ Pro W3', 'Hiragino Kaku Gothic Pro', 'メイリオ',
        Meiryo, Osaka, 'MSPゴシック', 'MS PGothic', sans-serif;
    -webkit-text-size-adjust: none;
    width: 100%;
}

#id {
    position: relative;
    height: auto !important; /*IE6対策*/
    height: 100%; /*IE6対策*/
    min-height: 100%;
}
</style>
