<template>
    <div class="wrapper">
        <div class="relic-list">
            <draggable
                v-model="relics"
                group="items"
                item-key="id"
                handle=".handle"
            >
                <template #item="{element}">
                    <div :class="element.quality">
                        <span class="handle">
                            <img
                                :src="element.icon"
                                :alt="element.jaName"
                                width="50"
                                height="50"
                            />
                        </span>
                    </div>
                </template>
            </draggable>

            <div class="user-belongings">
                <draggable
                    v-model="belongings"
                    group="items"
                    item-key="id"
                    handle=".handle"
                >
                    <template #item="{element}">
                        <div :class="element.quality">
                            <span class="handle">
                                <img
                                    :src="element.icon"
                                    :alt="element.jaName"
                                    width="50"
                                    height="50"
                                />
                            </span>
                        </div>
                    </template>
                </draggable>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue'
import draggable from 'vuedraggable'
import axios from '../../export'

interface Relic {
    id: string
    enName: string
    jaName: string
    quality: string
    compornent1: string
    compornent2: string
    compornent3: string
    compornent4: string
    cost: number
    totalPrice: number
    icon: string
}

export default defineComponent({
    components: {
        draggable
    },
    setup() {
        const relics = ref<Relic[]>([])
        const belongings = ref<Relic[]>([])

        axios
            .get('relic_calculator/relics')
            .then(response => {
                relics.value = response.data
            })
            .catch(error => {
                console.log(error.response)
            })

        return {
            relics,
            belongings
        }
    }
})
</script>
<style>
.relic-list {
    width: auto;
    height: auto;
}
.Common {
    display: inline-block;
}
.Rare {
    display: inline-block;
}
.Elite {
    display: inline-block;
}
.user-belongings {
    background: palegreen;
    width: 480px;
    height: 300px;
}
</style>
