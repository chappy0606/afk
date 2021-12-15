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
        <div class="relic-list">
            <draggable
                v-model="filteredRelics"
                :group="{ name: 'items', pull: 'clone',put:false }"
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
                    v-model="changeOrderRelics"
                    :group="{ name: 'items'}"
                    :sort="false"
                    item-key="id"
                    handle=".handle"
                    tag="transition-group"
                >
                    <template #item="{element,index}">
                        <div :class="element.quality">
                            {{index}}
                            <span class="handle">
                                <img
                                    :src="element.icon"
                                    :alt="element.jaName"
                                    width="50"
                                    height="50"
                                />
                                <span class="delete-button" @click="removeRelic(index)">×</span>
                            </span>
                        </div>
                    </template>
                </draggable>
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
        const relics = ref<Relic[]>([])
        const belongings = ref<Relic[]>([])
        const quality = ref<string>('')
        const searchWord = ref<string>('')

        const filteredRelics = computed({
            set: value => (relics.value = value),
            get: () => {
                if (searchWord.value) {
                    return relics.value
                        .filter(relic =>
                            relic.jaName.includes(searchWord.value)
                        )
                        .filter(relic => relic.quality.includes(quality.value))
                }
                return relics.value.filter(relic =>
                    relic.quality.includes(quality.value)
                )
            }
        })

        const changeOrderRelics = computed({
            set: value => {
                return belongings.value = value},
            get: () => {
                return belongings.value.slice().sort((a, b) => Number(a.id) - Number(b.id))
            }
        })

        const removeRelic = (index:number) => {
            // クリック時点では最後の値がsortされていない
            belongings.value.sort((a, b) => Number(a.id) - Number(b.id)).splice(index,1)
        }

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
            belongings,
            quality,
            searchWord,
            filteredRelics,
            changeOrderRelics,
            removeRelic
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
