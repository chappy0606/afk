<template>
    <div>
        <router-link :to="{ name: 'Upload' }">投稿ページ</router-link>
        <ChapterStageSelect @sendChapterStage="setChapterStage" />
        <template v-if="state.items">
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
        let chapter:string = ''
        let stage:string = ''

        const route = useRoute()

        const state: State = reactive({
            items: ''
        })

        const setChapterStage = (value: string): void => {
            if (value.includes('chapter')) {
                chapter = value.replace(/[^0-9]/g, '')
            } else if (value.includes('stage')) {
                stage = value.replace(/[^0-9]/g, '')
            }

            if (chapter && stage) {
                fetchPosts()
            }
        }

        const fetchPosts = (): void => {
            axios
                .get(
                    'https://127.0.0.1:8000/api/v1/campaign/posts/?chapter_id=' +
                        chapter +
                        '&stage_id=' +
                        stage
                )
                .then(response => {
                    router.push({
                        name: 'PveComp',
                        query: {
                            chapter_id: chapter,
                            stage_id: stage
                        }
                    })
                    if (response.data.length) {
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

        if (route.query.chapter_id && route.query.stage_id) {
            chapter = route.query.chapter_id.toString()
            stage = route.query.stage_id.toString()
            fetchPosts()
        }

        return {
            state,
            setChapterStage
        }
    }
})
</script>