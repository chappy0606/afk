<template>
    <div>
        <p>{{ getChapter() }}</p>
    </div>
</template>

<script lang="ts">
import { defineComponent,} from "vue";
import axios from "axios";

export default defineComponent({

    setup() {
        const getChapter = () => {
            axios.get("http://127.0.0.1:8000/api/v1/chapter/")
            .then(response => console.log(response))
            .catch(error => console.log(error));
        };
        return{
            getChapter,
        }
    }
})
</script>
