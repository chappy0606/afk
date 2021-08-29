<template>
    <div>
        <h2>Upload</h2>
        <ChapterStageSelect @sendChapterStage="setChapterStage" />
        <input type="file" accept="image/*" @change="setImageFile" v-if="showFlag" />
        <div v-if="url">
            <div class='preview-box'>
                <img :src="url" />
                <button @click="deletePreview">クリア</button>
            </div>
        </div>
        <button type="button" @click="registration">登録テスト</button>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent, ref, nextTick } from 'vue'
import { useStore } from '../../store'
import ChapterStageSelect from '../modules/ChapterStageSelect.vue'

export default defineComponent({
    components: { ChapterStageSelect },

    setup() {
        let url = ref('')
        let showFlag = ref(true)

        const store = useStore()
        const data = new FormData()
        data.append('user', String(store.state.authUser.user.id))

        const setChapterStage = (value: string): void => {
            if (value.includes('chapter')) {
                data.append('chapter_id', value.replace(/[^0-9]/g, ''))
            } else if (value.includes('stage'))
                data.append('stage_id', value.replace(/[^0-9]/g, ''))
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
                    console.log(error)
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
                .then(response => {
                    // 処理後リダイレクトする
                    console.log(response)
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