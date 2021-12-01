<template>
    <div>
        <li v-for="(value,key) in relics" :key="key">
            <img :src="value.icon" width="50" height="50">
        </li>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
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
interface Array {
    relics: Relic[]
}

export default defineComponent({
    setup() {
        const relics = ref<Array[]>([])

        axios.get('relic_calculator/relics').then(response => {
            relics.value = response.data
        })
        return {
            relics
        }
    }
})
</script>
