<template>
    <div id="app">
        <div class="footer-fixed">
            <Header />
            <router-view />
            <Footer />
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Header from './components/modules/Header.vue'
import Footer from './components/modules/Footer.vue'

export default defineComponent({
    components: { Header, Footer }
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
        Meiryo, Osaka, 'ＭＳ Ｐゴシック', 'MS PGothic', sans-serif;
    -webkit-text-size-adjust: none;
    width: 100%;
}

.footer-fixed {
    min-height: 100vh;
    position: relative;
    padding-bottom: 30%;
    box-sizing: border-box;
}
</style>
