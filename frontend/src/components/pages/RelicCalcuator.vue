<template>
    <div>
        <li v-for="(relic, key) in test" :key="key">
            <img :src="relic.icon" width="50" height="50" :alt="relic.jaName" />
        </li>
    </div>
</template>

<script lang="ts">
import { defineComponent, computed, ref } from 'vue'
import axios from '../../export'

interface Relic {
        id: string
        enName: string
        jaName: string
        quality: string
        compornent1: string
        compornent2: string
        compornent3: string
        compornent4: string
        cost: number
        totalPrice: number
        icon: string
}

export default defineComponent({
    setup() {
        const relics = ref<Relic[]>([])

        axios
            .get('relic_calculator/relics')
            .then(response => {
                relics.value = response.data
            })
            .catch(error => {
                console.log(error.response)
            })

        const test = computed(() => {
            return relics.value.filter((relic) => relic.quality.includes('Common'))
        })

        return {
            test
        }
    }
})
</script>
<style>
li {
    list-style: none;
}
</style>
