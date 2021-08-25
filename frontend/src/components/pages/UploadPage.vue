<template>
    <div>
        <h2>Upload</h2>
        <ChapterStageSelect @selectedChapterStage="setChapterStage" />
        <input type="file" @change="setImageFile" />
        <button type="button" @click="registration">登録テスト</button>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent, ref } from 'vue'
import { useStore } from '../../store'
import ChapterStageSelect from '../modules/ChapterStageSelect.vue'

export default defineComponent({
    components: { ChapterStageSelect },

    setup() {
        const store = useStore()
        const data = new FormData()

        const chapter = ref('')
        const stage = ref('')
        const image_file = ref<File>()

        const setChapterStage = (value: string): void => {
            if (value.includes('chapter')) {
                chapter.value = value.replace(/[^0-9]/g, '')
            } else if (value.includes('stage'))
                stage.value = value.replace(/[^0-9]/g, '')
        }

        const setImageFile = (event: { target: HTMLInputElement }): void => {
            if (
                event.target instanceof HTMLInputElement &&
                event.target.files
            ) {
                image_file.value = event.target.files[0]
            }
        }

        const registration = (): void => {
            data.append('user', String(store.state.authUser.user.id))
            data.append('chapter_id', chapter.value)
            data.append('stage_id', stage.value)
            data.append('uploaded_image', image_file.value)

            axios
                .post('https://127.0.0.1:8000/api/v1/campaign/posts/', data, {
                    headers: {
                        Authorization:
                            'JWT ' + store.state.authUser.access_token,
                        'content-type': 'multipart/form-data'
                    }
                })
                .then(response => {
                    console.log(response)
                })
        }

        return {
            setChapterStage,
            setImageFile,
            registration
        }
    }
})
</script>
