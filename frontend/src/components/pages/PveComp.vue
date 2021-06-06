<template>
    <div>
        <input
            type="text"
            placeholder="chapter..."
            list="chapter"
            v-on:change="test"
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
            v-on:change="test"
        />
        <datalist id="stage">
            <option v-for="stage in state.stageList" :key="stage.id">
                stage{{ stage.id }}
            </option>
        </datalist>
    </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue'
import axios from 'axios'

interface State {
    chpaterList: string
    stageList: string
}

export default defineComponent({
    setup() {
        const state: State = reactive({
            chpaterList: '',
            stageList: ''
        })
        
        axios
            .get('http://127.0.0.1:8000/api/v1/campaign/chapter/')
            .then(response => (state.chpaterList = response.data)),
        axios
            .get('http://127.0.0.1:8000/api/v1/campaign/stage/')
            .then(response => (state.stageList = response.data))

        const test = (test: { target: HTMLButtonElement }) => {
            console.log(test.target.value)
            console.log(test.target.value.replace(/[^0-9]/g, ''))
        }

        return {
            state,
            test
        }
    }
})
</script>
