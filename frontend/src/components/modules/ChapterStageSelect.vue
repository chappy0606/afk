<template>
    <div>
        <select v-model="state.selectedChapter" @change="sendChapterStage">
            <option v-for="chapter in state.chapters" :key="chapter.id">
                chapter{{ chapter.id }}
            </option>
        </select>
        <select v-model="state.selectedStage" @change="sendChapterStage">
            <option v-for="stage in state.stages" :key="stage.id">
                stage{{ stage.id }}
            </option>
        </select>
    </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'

interface State {
    chapters: string
    stages: string
    selectedChapter: string
    selectedStage: string
}

export default defineComponent({
    setup(props, { emit }) {
        const state: State = reactive({
            chapters: '',
            stages: '',
            selectedChapter: '',
            selectedStage: ''
        })

        const route = useRoute()

        axios
            .get('https://127.0.0.1:8000/api/v1/campaign/chapters/')
            .then(response => (state.chapters = response.data))
        axios
            .get('https://127.0.0.1:8000/api/v1/campaign/stages/')
            .then(response => (state.stages = response.data))

        if (route.query.chapter_id && route.query.stage_id) {
            state.selectedChapter = 'chapter' + route.query.chapter_id.toString()
            state.selectedStage = 'stage' + route.query.stage_id.toString()
        }

        const sendChapterStage = (event: {
            target: HTMLButtonElement
        }): void => {
            if (event.target.value) {
                emit('sendChapterStage', event.target.value)
            }
        }

        return {
            state,
            sendChapterStage
        }
    }
})
</script>