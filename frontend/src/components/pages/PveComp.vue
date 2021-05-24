<template>
    <div>
        {{ getChapter() }}
        <p>{{ state }}}</p>
    </div>
</template>

<script lang="ts">
import { defineComponent, reactive} from "vue";
import axios from "axios";

interface Chapter {
    chpaterList: number;
}

export default defineComponent({
    setup() {
        const state = reactive<Chapter>({
            chpaterList: 0
        });
        const getChapter = () => {
            axios
                .get("http://127.0.0.1:8000/api/v1/chapter/")
                .then(response => (state.chpaterList = response.data))
                .catch(error => console.log(error));
        };
        return {
            getChapter,
            state
        };
    }
});
</script>