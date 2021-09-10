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

        const test = (a: [], b: []): void => {
            let chapter: string
            let stage: string
            
            if (route.query.stage_id && route.query.stage_id) {
                chapter = String(route.query.chapter_id)
                stage = String(route.query.stage_id)

                // api側のlengthと入力された数値で比較してapi側以下ならselectに代入
                if (Number(chapter) <= a.length && b.length >= Number(stage)) {
                    state.selectedChapter = 'chapter' + chapter.toString()
                    state.selectedStage = 'stage' + stage.toString()
                } else {
                    router.push({
                        name: 'PveComp'
                    })
                }
            }
        }

        Promise.all([
            axios.get('https://127.0.0.1:8000/api/v1/campaign/chapters/'),
            axios.get('https://127.0.0.1:8000/api/v1/campaign/stages/')
        ]).then(([chapters, stages]) => {
            state.chapters = chapters.data
            state.stages = stages.data

            test(state.chapters, state.stages)
        })

        const sendChapterStage = (event: {
            target: HTMLButtonElement
        }) => {
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
