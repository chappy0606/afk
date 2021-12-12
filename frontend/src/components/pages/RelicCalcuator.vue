<template>
    <div>
        <div class="quality-nav">
            <label><input type="radio" value="" v-model="quality" />All</label>
            <label
                ><input
                    type="radio"
                    value="Common"
                    v-model="quality"
                />Common</label
            >
            <label
                ><input
                    type="radio"
                    value="Rare"
                    v-model="quality"
                />Rare</label
            >
            <label
                ><input
                    type="radio"
                    value="Elite"
                    v-model="quality"
                />Elite</label
            >
            <input type="text" v-model="searchWord" />
        </div>
        <div class="row">
        <div class="relic-list">
            <draggable
                v-model="filteredRelics"
                :group="{name:'items', pull:'clone'}"
                :sort="false"
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
    </div>
</template>

<script lang="ts">
import { computed, defineComponent, ref, watch } from 'vue'
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
        const RELICS = ref<Relic[]>([])
        const relics = ref<Relic[]>([])
        const belongings = ref<Relic[]>([])
        const quality = ref<string>('')
        const searchWord = ref<string>('')

        const initailRelics = () =>{
            relics.value = RELICS.value
        }

        watch(quality, () => initailRelics())

        watch(searchWord, () => initailRelics())
        watch(belongings, () => initailRelics())

        const filteredRelics = computed({
            set: value => (relics.value = value),
            get: () => {
                if (searchWord.value) {
                    return relics.value
                        .filter(relic => relic.jaName.includes(searchWord.value))
                        .filter(relic => relic.quality.includes(quality.value))
                }

                return relics.value.filter(relic =>
                    relic.quality.includes(quality.value)
                )
            }
        })

        axios
            .get('relic_calculator/relics')
            .then(response => {
                RELICS.value = response.data
                relics.value = response.data
            })
            .catch(error => {
                console.log(error.response)
            })

        return {
            RELICS,
            relics,
            belongings,
            quality,
            searchWord,
            filteredRelics
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
