<template>
    <div>
        <select :value="state.selectedChapter" @change="sendChapterStage">
            <option v-for="chapter in state.chapters" :key="chapter.id">
                chapter{{ chapter.id }}
            </option>
        </select>
        <select :value="state.selectedStage" @change="sendChapterStage">
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
import router from '../../router'

interface State {
    chapters: []
    stages: []
    selectedChapter: string
    selectedStage: string
}

export default defineComponent({
    setup(props, { emit }) {
        const state: State = reactive({
            chapters: [],
            stages: [],
            selectedChapter: '',
            selectedStage: ''
        })

        const route = useRoute()

        const checkQueryValue = (chapters: [], stages: []): void => {
            if (route.query.stage_id && route.query.stage_id) {
                const queryChapter: number = Number(route.query.chapter_id)
                const queryStage: number = Number(route.query.stage_id)
                // 0の処理
                if (!queryChapter || !queryStage){
                    router.push({name: 'PveComp'})
                    return
                }
                // DBに存在してる数字ならselectboxにセット
                if (queryChapter <= chapters.length && queryStage <= stages.length){
                    state.selectedChapter = 'chapter' + queryChapter.toString()
                    state.selectedStage = 'stage' + queryStage.toString()
                }
            }
        }

        Promise.all([
            axios.get('https://127.0.0.1:8000/api/v1/campaign/chapters/'),
            axios.get('https://127.0.0.1:8000/api/v1/campaign/stages/')
        ]).then(([chapters, stages]) => {
            state.chapters = chapters.data
            state.stages = stages.data

            checkQueryValue(state.chapters, state.stages)
        })

        const sendChapterStage = (event: { target: HTMLButtonElement }) => {
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
