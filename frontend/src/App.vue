<template>
  <div id="app">
    <p>hello</p>
    <Footer/>
  </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue';
import Footer from './components/modules/Footer.vue';

export default defineComponent({
  name: 'App',
  components: {Footer}
});
</script>

<style>

* {
	margin: 0px;
	padding: 0px;
}

html,body {
	height: 100%;
}

body {
	background-color: rgb(82, 82, 82);
	font-family:"ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", "メイリオ", Meiryo, Osaka, 
  "ＭＳ Ｐゴシック", "MS PGothic", sans-serif;
	-webkit-text-size-adjust: none;
	width: 100%;
}

</style>