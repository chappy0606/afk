<template>
    <div>
        <router-link to="/pve_comp/upload">投稿ページ</router-link>
        <ChapterStageSelect @selectedChapterStage="fetchPosts" />
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
import ChapterStageSelect from '../modules/ChapterStageSelect.vue'
import router from '../../router/index'
import { useRoute } from 'vue-router'

interface State {
    items: string
}

export default defineComponent({
    components: { ChapterStageSelect },

    setup() {
        let chapterId: string
        let stageId: string

        const route = useRoute()

        const state: State = reactive({
            items: ''
        })

        if (route.query.chapter_id && route.query.stage_id) {
            chapterId = route.query.chapter_id.toString()
            stageId = route.query.stage_id.toString()
            
        }

        const fetchPosts = (value: string): void => {
            if (value.includes('chapter')) {
                chapterId = value.replace(/[^0-9]/g, '')
            } else if (value.includes('stage')) {
                stageId = value.replace(/[^0-9]/g, '')
            }
            if (chapterId && stageId) {
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
                        } else {
                            state.items = ''
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
        }

        // if (route.query.chapter_id && route.query.stage_id) {
        //     chapterId = route.query.chapter_id.toString()
        //     stageId = route.query.stage_id.toString()
        //     // state.selectedChapter = 'chapter' + chapter
        //     // state.selectedStage = 'stage' + stage
        // }

        return {
            state,
            fetchPosts
        }
    }
})
</script>
