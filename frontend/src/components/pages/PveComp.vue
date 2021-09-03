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
                    if (response.data.length) {
                        images.value = response.data
                        router.push({
                            name: 'PveComp',
                            query: {
                                chapter_id: chapter.value,
                                stage_id: stage.value
                            }
                        })
                    } else {
                        images.value = ''
                    }
                })
                .catch(error => {
                    console.log(error)
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
            const pattern = new RegExp(/^([1-9]\d*|1)$/)

            chapter.value = route.query.chapter_id.toString()
            stage.value = route.query.stage_id.toString()
            // api側でエラー返すここの処理なくなるはず
            if (chapter.value.match(pattern) && stage.value.match(pattern)) {
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
