<template>
    <div>
        <select v-model="state.selectedChapter" @change="getChapterStage">
            <option v-for="chapter in state.chpaterList" :key="chapter.id">
                chapter{{ chapter.id }}
            </option>
        </select>
        <select v-model="state.selectedStage" @change="getChapterStage">
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
import router from '@/router'
import store from '@/store'

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

        axios
            .get('http://127.0.0.1:8000/api/v1/campaign/chapter/')
            .then(response => (state.chpaterList = response.data))
        axios
            .get('http://127.0.0.1:8000/api/v1/campaign/stage/')
            .then(response => (state.stageList = response.data))

        let chapter_id = ''
        let stage_id = ''
        let aaa = ''
        let bbb = ''

        const getChapterStage = (event: { target: HTMLButtonElement }) => {
            if (event.target.value.includes('chapter')) {
                chapter_id = event.target.value.replace(/[^0-9]/g, '')
                aaa = event.target.value
            } else if (event.target.value.includes('stage')) {
                stage_id = event.target.value.replace(/[^0-9]/g, '')
                bbb = event.target.value
            }
            store.state
            if (chapter_id && stage_id) {
                axios
                    .get(
                        'http://127.0.0.1:8000/api/v1/campaign/posts/?chapter_id=' +
                            chapter_id +
                            '&stage_id=' +
                            stage_id
                    )
                    .then(response => {
                        router.push({path:'/pve_comp/', query: {chapter:aaa,stage:bbb}})
                        // 1件もレコードがない時、空を渡す
                        if (response.data.length == 0) {
                            state.items = ''
                        } else {
                            state.items = response.data
                        }
                    })
            }
        }
        return {
            state,
            getChapterStage
        }
    }
})
</script>
