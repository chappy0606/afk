<template>
    <div>
        <h2>Upload</h2>
        <select v-model="chapter" @change="test" name="A">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
        </select>
        <select v-model="stage" @change="test" name="B">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
        </select>
        <input type="file" @change="test2" />
        <button type="button" @click="registration">登録テスト</button>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent } from 'vue'
import { useStore } from '../../store'

export default defineComponent({
    setup() {
        const store = useStore()
        let chapter = ''
        let stage = ''
        const data = new FormData()

        const test = (event: { target: HTMLButtonElement }): void => {
            if (event.target.name === 'A') {
                chapter = event.target.value
                console.log(chapter)
            } else if (event.target.name === 'B') {
                stage = event.target.value
                console.log(stage)
            }
        }

        const test2 = (event: { target: HTMLInputElement }): void => {
            data.append('uploaded_image', event.target.files[0])
        }

        const registration = (): void => {
            data.append('chapter_id', chapter)
            data.append('stage_id', stage)
            data.append('user', String(store.state.authUser.user.id))
            console.log(data.get('chapter_id'))
            console.log(data.get('stage_id'))
            console.log(data.get('user'))
            console.log(data.get('uploaded_image'))

            axios
                .post(
                    'https://127.0.0.1:8000/api/v1/campaign/posts/',
                    
                    // {data}はエラー
                    data,
                    {
                        headers: {
                            Authorization:
                                'JWT ' + store.state.authUser.access_token,
                                'content-type': 'multipart/form-data'
                        }
                    }
                )
                .then(response => {
                    console.log(response)
                })
        }

        return {
            test,
            test2,
            registration
        }
    }
})
</script>
