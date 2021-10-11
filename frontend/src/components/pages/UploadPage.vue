<template>
    <div>
        <h2>Upload</h2>
        <ChapterStageSelect @sendChapterStage="setChapterStage" />
        <input
            type="file"
            accept="image/*"
            @change="setImageFile"
            v-if="shouldShow"
        />
        <div v-show="images" class="preview-box">
            <img :src="images" />
            <button @click="deletePreview">クリア</button>
        </div>
        <button @click="registration">登録テスト</button>
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
        const images = ref<string>('')
        const shouldShow = ref<boolean>(true)

        const store = useStore()

        const data = new FormData()

        const setChapterStage = (value: string): void => {
            if (value.includes('chapter')) {
                data.append('chapterId', value.replace(/[^0-9]/g, ''))
            } else if (value.includes('stage'))
                data.append('stageId', value.replace(/[^0-9]/g, ''))
        }

        const deletePreview = () => {
            images.value = ''
            data.delete('uploaded_image')
            shouldShow.value = false
            nextTick(() => shouldShow.value = true)
        }

        const setImageFile = (event: { target: HTMLInputElement }): void => {
            if (event.target instanceof HTMLInputElement && event.target.files) {
                try {
                    images.value = URL.createObjectURL(event.target.files[0])
                    data.append('uploaded_image', event.target.files[0])
                } catch {
                    deletePreview()
                }
            }
        }

        const registration = (): void => {
            data.append('user', String(store.state.authUser.user.id))

            axios
                .post('https://127.0.0.1:8000/api/v1/campaign/posts/', data, {
                    headers: {
                        Authorization:
                            'JWT ' + store.state.authUser.accessToken,
                            'content-type': 'multipart/form-data'
                    }
                })
                .then(() => {
                    router.push({
                        name: 'PveComp',
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
            images,
            deletePreview,
            shouldShow,
        }
    }
})
</script>
<style>
div.preview-box img {
    width: 50%;
    height: 50%;
}
</style>
