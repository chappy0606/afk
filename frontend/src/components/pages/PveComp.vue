<template>

    <div>
        <select v-model="selectedChapter">
            <option disabled value="">chapter</option>
            <option v-for="chapter in state.chpaterList" :key="chapter.id">
                {{ chapter.id }}
            </option>
        </select>
    </div>

</template>

<script lang="ts">
import { defineComponent, reactive, } from 'vue'
import axios from 'axios'

interface Chapter {
    chpaterList: number
}

export default defineComponent({
    setup() {

        const state = reactive<Chapter>({
            chpaterList: 0
        })

        axios
            .get('http://127.0.0.1:8000/api/v1/chapter/')
            .then(response => (state.chpaterList = response.data))

        return {
            state
        }
    }
})
</script>
