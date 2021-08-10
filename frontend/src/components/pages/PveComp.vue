<template>
    <div>
        <router-link to="/pve_comp/upload">投稿ページ</router-link>
        <select v-model="state.selectedChapter" @change="selectChapterStage">
            <option v-for="chapter in state.chpaters" :key="chapter.id">
                chapter{{ chapter.id }}
            </option>
        </select>
        <select v-model="state.selectedStage" @change="selectChapterStage">
            <option v-for="stage in state.stages" :key="stage.id">
                stage{{ stage.id }}
            </option>
        </select>
        <template v-if="state.items != ''">
            <li v-for="path in state.items" :key="path">
                <div id="postedImage">
                    <img :src="path.uploaded_image" />
                </div>
            </li>
        </template>
    </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue'
import axios from 'axios'
import router from '../../router/index'
import { useRoute } from 'vue-router'

interface State {
    chpaters: string
    stages: string
    selectedChapter: string
    selectedStage: string
    items: string
}

export default defineComponent({
    setup() {
        let chapterId: string
        let stageId: string

        const route = useRoute()

        const state: State = reactive({
            chpaters: '',
            stages: '',
            selectedChapter: '',
            selectedStage: '',
            items: ''
        })

        axios
            .get('https://127.0.0.1:8000/api/v1/campaign/chapters/')
            .then(response => (state.chpaters = response.data))
        axios
            .get('https://127.0.0.1:8000/api/v1/campaign/stages/')
            .then(response => (state.stages = response.data))

        const selectChapterStage = (event: {
            target: HTMLButtonElement
        }): void => {
            if (event.target.value.includes('chapter')) {
                chapterId = event.target.value.replace(/[^0-9]/g, '')
            } else if (event.target.value.includes('stage')) {
                stageId = event.target.value.replace(/[^0-9]/g, '')
            }

            if (chapterId && stageId) {
                getPosts(chapterId, stageId)
            }
        }

        const getPosts = (chapterId: string, stageId: string): void => {
            axios
                .get(
                    'https://127.0.0.1:8000/api/v1/campaign/posts/?chapter_id=' +
                        chapterId +
                        '&stage_id=' +
                        stageId
                )
                .then(response => {
                    router.push({
                        path: '/pve_comp/',
                        query: {
                            chapter_id: chapterId,
                            stage_id: stageId
                        }
                    })

                    if (response.data.length != 0) {
                        state.items = response.data
                    }
                })

                .catch(error => {
                    const {
                        status,
                        statusText
                    }: {
                        status: string
                        statusText: string
                    } = error.response
                    console.log('Error! HTTP Status:' + status + statusText)
                })
        }

        // URL直叩きの場合の処理
        if (route.query.chapter_id && route.query.stage_id) {
            chapterId = route.query.chapter_id.toString()
            stageId = route.query.stage_id.toString()

            state.selectedChapter = 'chapter' + chapterId
            state.selectedStage = 'stage' + stageId

            getPosts(chapterId, stageId)
        }

        return {
            state,
            selectChapterStage
        }
    }
})
</script>
