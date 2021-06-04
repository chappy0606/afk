<template>
    <div>
        <select v-model="selectChapterStage" v-on:change="test">
            <option disabled value="null">chapter...</option>
            <option v-for="chapter in state.chpaterList" :key="chapter.id">
                chapter{{ chapter.id }}
            </option>
        </select>
        <select v-model="selectChapterStage">
            <option disabled value="null">stage...</option>
            <option v-for="stage in state.stageList" :key="stage.id">
                stage{{ stage.id }}
            </option>
        </select>
    </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue'
import axios from 'axios'

interface State {
    chpaterList: number
    stageList: number
}

export default defineComponent({
    setup() {
        const state = reactive<State>({
            chpaterList: 0,
            stageList: 0
        })

        const selectChapterStage: string = null

        axios
            .get('http://127.0.0.1:8000/api/v1/campaign/chapter/')
            .then(response => (state.chpaterList = response.data)),
        axios
            .get('http://127.0.0.1:8000/api/v1/campaign/stage/')
            .then(response => (state.stageList = response.data))

        const test = (): void => {
            console.log('test')
        }

        // getChapterStage()

        return {
            state,
            selectChapterStage,
            test
        }
    }
})
</script>
