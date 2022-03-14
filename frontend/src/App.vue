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
}

#app {
    height: 100%;
    display: flex;
    flex-direction: column;
}

.active-component {
    flex: 1;
}

</style>
