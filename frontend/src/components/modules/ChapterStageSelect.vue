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
import { useRoute, onBeforeRouteUpdate, LocationQuery } from 'vue-router'
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

        const checkQuery = (query: LocationQuery) => {
            const queryChapter: number = Number(query.chapter_id)
            const queryStage: number = Number(query.stage_id)

            if(!queryChapter || !queryStage){
                return
            }

            if (queryChapter > state.chapters.length || queryStage > state.stages.length){
                return
            }

            state.selectedChapter = 'chapter' + queryChapter.toString()
            state.selectedStage = 'stage' + queryStage.toString()
            
            return query
        }

        Promise.all([
            axios.get('https://127.0.0.1:8000/api/v1/campaign/chapters/'),
            axios.get('https://127.0.0.1:8000/api/v1/campaign/stages/')
        ]).then(([chapters, stages]) => {
            state.chapters = chapters.data
            state.stages = stages.data
            emit('send-chapter-stages', state.chapters, state.stages)

            if (route.query.chapter_id && route.query.stage_id) {
                if(!checkQuery(route.query)){
                    router.push({name: 'PveComp'})
                }
            }
        })

        onBeforeRouteUpdate(to => {
            checkQuery(to.query)
            if (Number(to.query.stage_id) > state.stages.length){
                state.selectedChapter = ''
                state.selectedStage = ''
                router.push({name: 'PveComp'})
            }
        })

        const sendChapterStage = (event: { target: HTMLButtonElement }) => {
            if (event.target.value) {
                emit('selected-value-send', event.target.value)
            }
        }

        return {
            state,
            sendChapterStage
        }
    }
})
</script>
