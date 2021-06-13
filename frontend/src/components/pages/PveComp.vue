<template>
    <div>
        <input
            type="text"
            placeholder="chapter..."
            list="chapter"
            v-on:change="getChapterStage"
        />
        <datalist id="chapter">
            <option v-for="chapter in state.chpaterList" :key="chapter.id">
                chapter{{ chapter.id }}
            </option>
        </datalist>

        <input
            type="text"
            placeholder="stage..."
            list="stage"
            v-on:change="getChapterStage"
        />
        <datalist id="stage">
            <option v-for="stage in state.stageList" :key="stage.id">
                stage{{ stage.id }}
            </option>
        </datalist>
        <li v-for="path in state.items" :key="path.id">
            <div id="postedImage">
                <img :src="path.uploaded_image" />
            </div>
        </li>
    </div>
</template>

<script lang='ts'>
import { defineComponent, reactive } from 'vue'
import axios from 'axios'

interface State {
    chpaterList: string
    stageList: string
    items: string
}

export default defineComponent({
    
    setup() {
        const state: State = reactive({
            chpaterList: '',
            stageList: '',
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

        const getChapterStage = (event: { target: HTMLButtonElement }) => {
            if (event.target.value.includes('chapter')) {
                chapter_id = event.target.value.replace(/[^0-9]/g, '')
            } else if (event.target.value.includes('stage')) {
                stage_id = event.target.value.replace(/[^0-9]/g, '')
            }

            if (chapter_id && stage_id) {
                axios
                    .get(
                        'http://127.0.0.1:8000/api/v1/campaign/posts/?chapter_id=' +
                            chapter_id +
                            '&stage_id=' +
                            stage_id
                    )
                    .then(response => (state.items = response.data))
            }
        }

        return {
            state,
            getChapterStage,
        }
    }
})
</script>
