<template>
    <div>
        <router-link :to="{ name: 'Upload' }">投稿ページ</router-link>
        <ChapterStageSelect @sendChapterStage="setChapterStage" />
        <template v-if="images">
            <li v-for="path in images" :key="path">
                <div id="postedImage">
                    <img :src="path.uploaded_image" />
                </div>
            </li>
        </template>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import axios from 'axios'
import ChapterStageSelect from '../modules/ChapterStageSelect.vue'
import router from '../../router/index'
import { useRoute } from 'vue-router'

export default defineComponent({
    components: { ChapterStageSelect },

    setup() {
        let chapter = ref<string>('')
        let stage = ref<string>('')

        const images = ref<string>('')
        const route = useRoute()

        const fetchPosts = (): void => {
            axios
                .get(
                    'https://127.0.0.1:8000/api/v1/campaign/posts/?chapter_id=' +
                        chapter.value +
                        '&stage_id=' +
                        stage.value
                )
                .then(response => {
                    console.log(response.data)
                    if (response.data.length) {
                        images.value = response.data
                    } else {
                        images.value = ''
                    }
                    router.push({
                        name: 'PveComp',
                        query: {
                            chapter_id: chapter.value,
                            stage_id: stage.value
                        }
                    })
                })
                .catch(error => {
                    if (error.response.status === 400) {
                        router.push({
                            name: 'PveComp'
                        })
                    }
                })
        }

        const setChapterStage = (value: string): void => {
            if (value.includes('chapter')) {
                chapter.value = value.replace(/[^0-9]/g, '')
            } else if (value.includes('stage')) {
                stage.value = value.replace(/[^0-9]/g, '')
            }
            if (chapter.value && stage.value) {
                fetchPosts()
            }
        }

        if (route.query.chapter_id && route.query.stage_id) {
            chapter.value = route.query.chapter_id.toString()
            stage.value = route.query.stage_id.toString()

            if (chapter.value && stage.value) {
                fetchPosts()
            }
        }

        return {
            setChapterStage,
            images
        }
    }
})
</script>