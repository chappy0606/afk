<template>
    <div>
        <h2>Upload</h2>
        <ChapterStageSelect @selected-value-send="setChapterStage">
            <template v-slot:ChapterErrorMessage v-if="resp.chapterId">{{resp.chapterId}}</template>
            <template v-slot:StageErrorMessage v-if="resp.stageId">{{resp.stageId}}</template>
        </ChapterStageSelect>

        <input
            type="file"
            accept="image/*"
            @change="setImageFile"
            v-if="shouldShow"
        />
        <label v-if="resp.uploadedImage">{{ resp.uploadedImage }}</label>
        <div v-show="images" class="preview-box">
            <img :src="images" />
            <button @click="deletePreview">クリア</button>
        </div>
        <button @click="registration">登録テスト</button>
    </div>
</template>

<script lang="ts">
import axios from '../../export'
import { defineComponent, ref, nextTick, reactive } from 'vue'
import router from '../../router/index'
import { useStore } from '../../store'
import ChapterStageSelect from '../modules/ChapterStageSelect.vue'

interface ResponseData {
    chapterId: string
    stargeId: string
    uploadedImage: string
}

export default defineComponent({
    components: { ChapterStageSelect },

    setup() {
        const resp:ResponseData = reactive({
            chapterId: '',
            stargeId: '',
            uploadedImage: ''
        })

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
            nextTick(() => (shouldShow.value = true))
        }

        const setImageFile = (event: { target: HTMLInputElement }): void => {
            if (
                event.target instanceof HTMLInputElement &&
                event.target.files
            ) {
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
                .post('/campaign/posts/', data, {
                    headers: {
                        Authorization:
                            'JWT ' + store.state.authUser.accessToken,
                        'content-type': 'multipart/form-data'
                    }
                })
                .then(() => {
                    router.push({
                        name: 'PveComp'
                    })
                })
                .catch(error => {
                    for (const key in error.response.data){
                        resp[key as keyof ResponseData] = error.response.data[key][0]
                    }
                })
        }

        return {
            setChapterStage,
            setImageFile,
            registration,
            images,
            deletePreview,
            shouldShow,
            resp
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
