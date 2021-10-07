<template>
    <div>
        <router-link :to="{ name: 'Upload' }">投稿ページ</router-link>
        <ChapterStageSelect @sendChapterStage="setChapterStage" />
        <li v-for="path in images" :key="path">
            <div id="postedImage">
                <img :src="path.uploaded_image" />
            </div>
        </li>
    </div>
</template>

<script lang="ts">

import { defineComponent, ref, watchEffect } from 'vue'
import axios from 'axios'
import ChapterStageSelect from '../modules/ChapterStageSelect.vue'
import router from '../../router/index'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'

export default defineComponent({
    components: { ChapterStageSelect },

    setup() {
        const route = useRoute()

        const chapter = ref<string>()
        const stage = ref<string>()
        const images = ref<string>()

        const setChapterStage = (value: string): void => {
            if (value.includes('chapter')) {
                chapter.value = value.replace(/[^0-9]/g, '')
            } else if (value.includes('stage')) {
                stage.value = value.replace(/[^0-9]/g, '')
            }
        }

        if (route.query.chapter_id && route.query.stage_id) {
            chapter.value = route.query.chapter_id.toString()
            stage.value = route.query.stage_id.toString()
        } else {
            router.push({
                name: 'PveComp'
            })
        }

        onBeforeRouteUpdate(to => {
            if (to.query.chapter_id && to.query.stage_id) {
                chapter.value = to.query.chapter_id.toString()
                stage.value = to.query.stage_id.toString()
            }
        })

        watchEffect(() => {
            if (chapter.value && stage.value) {
                axios
                    .get(
                        'https://127.0.0.1:8000/api/v1/campaign/posts/?chapter_id=' +
                            chapter.value +
                            '&stage_id=' +
                            stage.value
                    )
                    .then(response => {
                        images.value = response.data
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
        })

        return {
            setChapterStage,
            images
        }
    }
})
</script>
