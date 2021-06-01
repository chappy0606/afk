<template>
    <div>
        <select v-model="selectChapterStage">
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

interface ChapterStage {
    chpaterList: number
    stageList: number
}

export default defineComponent({
    setup() {
        const state = reactive<ChapterStage>({
            chpaterList: 0,
            stageList: 0
        })

        const selectChapterStage: string = null

        const getChapterStage = (): void => {
            axios
                .get('http://127.0.0.1:8000/api/v1/chapter/')
                .then(response => (state.chpaterList = response.data)),
            axios
                .get('http://127.0.0.1:8000/api/v1/stage/')
                .then(response => (state.stageList = response.data))
        }

        getChapterStage()

        return {
            state,
            selectChapterStage
        }
    }
})
</script>