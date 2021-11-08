<template>
    <div>
        <router-link :to="{ name: 'Upload' }">投稿ページ</router-link>
        <button v-if="stage > 1" @click="fetchPrevStage">前へ</button>
        <button v-if="1 <= stage && stage < stages.length" @click="fetchNextStage">次へ</button>
        <ChapterStageSelect @selected-value-send="setChapterStage" @send-chapter-stages="setChapterStageList" />
        <li v-for="path in images" :key="path">
            <img :src="path.uploadedImage" />
        </li>
    </div>
</template>

<script lang="ts">

import { defineComponent, ref, watchEffect } from 'vue'
import axios from '../../export'
import ChapterStageSelect from '../modules/ChapterStageSelect.vue'
import router from '../../router/index'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'

export default defineComponent({
    components: { ChapterStageSelect },

    setup() {
        const route = useRoute()

        const chapter = ref<string>('')
        const stage = ref<string>('')

        const chapters = ref<string[]>([])
        const stages = ref<string[]>([])

        const images = ref<string>('')

        const setChapterStage = (value: string): void => {
            if (value.includes('chapter')) {
                chapter.value = value.replace(/[^0-9]/g, '')
            } else if (value.includes('stage')) {
                stage.value = value.replace(/[^0-9]/g, '')
            }
        }

        const fetchNextStage = ():void => {
            if(Number(stage.value) < chapters.value.length){
                stage.value = (Number(route.query.stage_id) + 1).toString()
            }
        }

        const fetchPrevStage = ():void => {
            if(Number(stage.value) < chapters.value.length){
                stage.value = (Number(route.query.stage_id) - 1).toString()
            }
        }

        const setChapterStageList = (ch:[],st:[]):void => {
            chapters.value = ch
            stages.value = st
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
            images,
            stages,
            stage,
            fetchNextStage,
            fetchPrevStage,
            setChapterStageList
        }
    }
})
</script>
