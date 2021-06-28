<template>
    <div>
        <router-link to="/pve_comp/upload">投稿ページ</router-link>
        <select v-model="state.selectedChapter" @change="selectChapterStage">
            <option v-for="chapter in state.chpaterList" :key="chapter.id">
                chapter{{ chapter.id }}
            </option>
        </select>
        <select v-model="state.selectedStage" @change="selectChapterStage">
            <option v-for="stage in state.stageList" :key="stage.id">
                stage{{ stage.id }}
            </option>
        </select>

        <li v-for="path in state.items" :key="path">
            <div id="postedImage">
                <img :src="path.uploaded_image" />
            </div>
        </li>
    </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue'
import axios from 'axios'
import router from '../../router/index'
// import router from '@/router afkからvscode開くとエラー(pathの問題)'
import { useRoute } from 'vue-router'

interface State {
    chpaterList: string
    stageList: string
    selectedChapter: string
    selectedStage: string
    items: string
}

export default defineComponent({
    setup() {
        const state: State = reactive({
            chpaterList: '',
            stageList: '',
            selectedChapter: '',
            selectedStage: '',
            items: ''
        })

        let chapterId: string
        let stageId: string

        const route = useRoute()

        // get時chapterとstage取得
        axios
            .get('https://localhost:8000/api/v1/campaign/chapter/')
            .then(response => (state.chpaterList = response.data))
        axios
            .get('https://localhost:8000/api/v1/campaign/stage/')
            .then(response => (state.stageList = response.data))

        //  onChange
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
                    'http://127.0.0.1:8000/api/v1/campaign/posts/?chapter_id=' +
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

                    // 1件もレコードがない時、空を渡す
                    if (response.data.length == 0) {
                        state.items = ''
                    } else {
                        state.items = response.data
                        // onChange以外の場合、sekectの更新
                        state.selectedChapter = 'chapter' + chapterId
                        state.selectedStage = 'stage' + stageId
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

        // 直接URLにクエリsetされた時の処理
        if (route.query.chapter_id && route.query.stage_id) {
            chapterId = route.query.chapter_id.toString()
            stageId = route.query.stage_id.toString()
            getPosts(chapterId, stageId)
        }

        return {
            state,
            selectChapterStage
        }
    }
})
</script>
