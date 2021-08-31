<template>
    <div>
        <h2>Upload</h2>
        <ChapterStageSelect @sendChapterStage="setChapterStage" />
        <input type="file" accept="image/*" @change="setImageFile" v-if="showFlag" />
        <div v-show="url" class='preview-box'>
            <img :src="url" />
            <button @click="deletePreview">クリア</button>
            </div>
        <button type="button" @click="registration">登録テスト</button>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent, ref, nextTick } from 'vue'
import router from '../../router/index'
import { useStore } from '../../store'
import ChapterStageSelect from '../modules/ChapterStageSelect.vue'

export default defineComponent({
    components: { ChapterStageSelect },

    setup() {
        let url = ref<string>('')
        let showFlag = ref<boolean>(true)
        let chapter: string = ''
        let stage: string = ''

        const store = useStore()
        
        const data = new FormData()
        data.append('user', String(store.state.authUser.user.id))

        const setChapterStage = (value: string): void => {
            if (value.includes('chapter')) {
                chapter = value.replace(/[^0-9]/g, '')
                data.append('chapter_id', chapter)
            } else if (value.includes('stage'))
                stage = value.replace(/[^0-9]/g, '')
                data.append('stage_id', stage)
        }

        const deletePreview = () => {
            url.value = ''
            data.delete('uploaded_image')
            showFlag.value = false
            nextTick(() => showFlag.value = true)
        }

        const setImageFile = (event: { target: HTMLInputElement }): void => {
            if (
                event.target instanceof HTMLInputElement &&
                event.target.files
            ) {
                try {
                    url.value = URL.createObjectURL(event.target.files[0])
                    data.append('uploaded_image', event.target.files[0])
                } catch (error) {
                    deletePreview()
                }
            }
        }

        const registration = (): void => {
            axios
                .post('https://127.0.0.1:8000/api/v1/campaign/posts/', data, {
                    headers: {
                        Authorization:
                            'JWT ' + store.state.authUser.access_token,
                            'content-type': 'multipart/form-data'
                    }
                })
                .then( () =>{
                    router.push({
                        name: 'PveComp',
                        query: {
                            chapter_id: chapter,
                            stage_id: stage
                        }
                    })
                })
                .catch(error => {
                    console.log(error)
                })
        }

        return {
            setChapterStage,
            setImageFile,
            registration,
            url,
            deletePreview,
            showFlag
        }
    }
})
</script>
<style>
div.preview-box img{
    width: 50%;
    height: 50%;
}
</style>