<template>
    <div>
        <router-link to="/pve_comp/upload">投稿ページ</router-link>
        <ChapterStageSelect @selectedChapterStage="setChapterStage" />
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
import { defineComponent, reactive, ref } from 'vue'
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
        const route = useRoute()

        const state: State = reactive({
            items: ''
        })

        const chapterId = ref<string>('')
        const stageId = ref<string>('')

        const setChapterStage = (value: string): void => {
            if (value.includes('chapter')) {
                chapterId.value = value.replace(/[^0-9]/g, '')
            } else if (value.includes('stage')) {
                stageId.value = value.replace(/[^0-9]/g, '')
            }
            if (chapterId.value && stageId.value) {
                fetchPosts()
            }
        }

        const fetchPosts = (): void => {
            axios
                .get(
                    'https://127.0.0.1:8000/api/v1/campaign/posts/?chapter_id=' +
                        chapterId.value +
                        '&stage_id=' +
                        stageId.value
                )
                .then(response => {
                    router.push({
                        path: '/pve_comp/',
                        query: {
                            chapter_id: chapterId.value,
                            stage_id: stageId.value
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

        if (route.query.chapter_id && route.query.stage_id) {
            chapterId.value = route.query.chapter_id.toString()
            stageId.value = route.query.stage_id.toString()
            fetchPosts()
        }
        
        return {
            state,
            setChapterStage
        }
    }
})
</script>
