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
                :group="{ name: 'items', pull: 'clone', put: false }"
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
                    :group="{ name: 'items' }"
                    :sort="false"
                    item-key="id"
                    handle=".handle"
                    tag="transition-group"
                >
                    <template #item="{element,index}">
                        <div :class="element.quality">
                            <span class="handle" v-if="element.icon">
                                <img
                                    :src="element.icon"
                                    :alt="element.jaName"
                                    width="50"
                                    height="50"
                                />
                                <label>{{ element.count }}</label>
                                <button
                                    class="add-button"
                                    @click="addRelic(index)"
                                >
                                    +
                                </button>
                                <button
                                    class="remove-button"
                                    @click="removeRelic(index)"
                                >
                                    -
                                </button>
                            </span>
                        </div>
                    </template>
                </draggable>
                {{ sumArray }}
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { computed, defineComponent, ref, resolveDirective, watch } from 'vue'
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
interface Belongings extends Relic {
    count: number
}

export default defineComponent({
    components: {
        draggable
    },
    setup() {
        const relics = ref<Relic[]>([])
        const belongings = ref<Belongings[]>([])
        const quality = ref<string>('')
        const searchWord = ref<string>('')

        const filteredRelics = computed({
            get: () => {
                return relics.value
                    .filter(relic => relic.jaName.includes(searchWord.value))
                    .filter(relic => relic.quality.includes(quality.value))
            },
            set: value => relics.value = value
        })

        const changeOrderRelics = computed({
            get: () => belongings.value,
            set: value => {
                belongings.value = value
                    .filter((x, i, self) => {
                        if (typeof x.count === 'undefined' || x.count <= 0) {
                            x.count = 1
                        }
                        return self.indexOf(x) === i
                    })
                    .sort((a, b) => Number(a.id) - Number(b.id))
            }
        })

        const sumArray = computed(() => {
            let sum: number = 0
            for (let i in belongings.value) {
                console.log(
                    belongings.value[i].jaName + belongings.value[i].totalPrice
                )
                console.log(belongings.value[i].count)
                sum +=
                    belongings.value[i].totalPrice * belongings.value[i].count
            }
            console.log(sum)
            return sum
        })

        const addRelic = (index: number) => {
            belongings.value[index].count++
        }

        const removeRelic = (index: number) => {
            belongings.value[index].count--

            if (belongings.value[index].count <= 0) {
                belongings.value.splice(index, 1)
            }
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
            removeRelic,
            addRelic,
            sumArray
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
    width: auto;
    height: auto;
}
</style>
