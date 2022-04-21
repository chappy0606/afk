<template>
    <div>
        <div class="quality-nav">
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
        <vue-element-loading :active="isLoading" :is-full-screen="true" />
        <draggable
            v-model="filteredRelics"
            :group="{ name: 'items', pull: 'clone', put: false }"
            :sort="false"
            :clone="cloneRelic"
            item-key="id"
            handle=".handle"
        >
            <template #item="{ element }">
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

        <div class="wrapper-box">
            <div class="belongings">
                <draggable
                    v-model="filteredbelongings"
                    :group="{ name: 'items' }"
                    :sort="false"
                    item-key="id"
                    handle=".handle"
                    tag="transition-group"
                >
                    <template #item="{ element, index }">
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
                                    id="belongings-add-btn"
                                    @click="addCount($event, index)"
                                >
                                    +
                                </button>
                                <button
                                    id="belongings-sub-btn"
                                    @click="subtractCount($event, index)"
                                >
                                    -
                                </button>
                            </span>
                        </div>
                    </template>
                </draggable>
            </div>

            <div class="necessary-relic">
                <draggable
                    v-model="filterednecessaryRelics"
                    :group="{ name: 'items' }"
                    :sort="false"
                    item-key="id"
                    handle=".handle"
                    tag="transition-group"
                >
                    <template #item="{ element, index }">
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
                                    id="necessary-relic-add-btn"
                                    @click="addCount($event, index)"
                                >
                                    +
                                </button>
                                <button
                                    id="necessary-relic-sub-btn"
                                    @click="subtractCount($event, index)"
                                >
                                    -
                                </button>
                            </span>
                        </div>
                    </template>
                </draggable>
            </div>
        </div>
        不必要な遺物:
        <p v-for="(num, relic) in unnecessaryRelics" :key="relic">
            {{ relic }}:{{ num }}個
        </p>
        合計エッセンス:{{ totalCost }}
    </div>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue'
import draggable from 'vuedraggable'
import VueElementLoading from 'vue-element-loading'
import axios from '../../export'

interface Relic {
    id: string
    enName: string
    jaName: string
    quality: string
    component1: string
    component2: string
    component3: string
    component4: string
    cost: number
    totalPrice: number
    icon: string
    count: number
}
interface Counter {
    [key: string]: number
}
export default defineComponent({
    components: {
        draggable,
        VueElementLoading,
    },

    setup() {
        const relics = ref<Relic[]>([])
        const belongings = ref<Relic[]>([])
        const necessaryRelics = ref<Relic[]>([])
        const quality = ref<string>('Common')
        const searchWord = ref<string>('')
        const isLoading = ref<boolean>(true)

        const filteredRelics = computed({
            get: () => {
                return relics.value
                    .filter((relic) => {
                        return (
                            relic.enName
                                .toLowerCase()
                                .includes(searchWord.value.toLowerCase()) ||
                            relic.jaName.includes(searchWord.value)
                        )
                    })
                    .filter((relic) => relic.quality.includes(quality.value))
            },
            set: (value) => (relics.value = value),
        })

        const filterRelics = (array: Relic[]) => {
            return array
                .filter((relic, index, array) => {
                    if (
                        typeof relic.count === 'undefined' ||
                        relic.count <= 0
                    ) {
                        relic.count = 1
                    }
                    return array.findIndex((v) => relic.id === v.id) === index
                })
                .sort((a, b) => Number(a.id) - Number(b.id))
        }

        const filteredbelongings = computed({
            get: () => {
                return belongings.value
            },
            set: (value) => {
                return (belongings.value = filterRelics(value))
            },
        })

        const filterednecessaryRelics = computed({
            get: () => necessaryRelics.value,
            set: (value) => (necessaryRelics.value = filterRelics(value)),
        })

        const removeRelic = (array: Relic[], index: number): void => {
            if (array[index].count <= 0) {
                array.splice(index, 1)
            }
        }

        const addCount = (
            event: { target: HTMLInputElement },
            index: number
        ): void => {
            if (event.target.id === 'belongings-add-btn') {
                belongings.value[index].count++
            } else if (event.target.id === 'necessary-relic-add-btn') {
                necessaryRelics.value[index].count++
            }
        }

        const subtractCount = (
            event: { target: HTMLInputElement },
            index: number
        ): void => {
            if (event.target.id === 'belongings-sub-btn') {
                belongings.value[index].count--
                removeRelic(belongings.value, index)
            } else if (event.target.id === 'necessary-relic-sub-btn') {
                necessaryRelics.value[index].count--
                removeRelic(necessaryRelics.value, index)
            }
        }

        const cloneRelic = (value: Relic) => {
            return {
                id: value.id,
                enName: value.enName,
                jaName: value.jaName,
                quality: value.quality,
                component1: value.component1,
                component2: value.component2,
                component3: value.component3,
                component4: value.component4,
                cost: value.cost,
                totalPrice: value.totalPrice,
                icon: value.icon,
                count: value.count,
            }
        }

        const countDuplicates = (array: string[]): Counter => {
            return array.filter(Boolean).reduce((prev, current) => {
                prev[current] = (prev[current] || 0) + 1
                return prev
            }, {} as Partial<Counter>) as Counter
        }

        const getRelics = (array: Relic[]): Counter => {
            const relics: string[] = []
            array.filter((relic) => {
                for (let i = 0; i < relic.count; i++) {
                    relics.push(relic.jaName)
                }
            })
            return countDuplicates(relics)
        }

        const getComponents = (obj: Counter): Counter => {
            const components: string[] = []
            const array = getRelicDetails(obj)

            array.filter((relic) => {
                for (let i = 0; i < relic.count; i++) {
                    components.push(
                        relic.component1,
                        relic.component2,
                        relic.component3,
                        relic.component4
                    )
                }
            })
            return countDuplicates(components)
        }

        const getRelicDetails = (obj: Counter) => {
            const relicsDetails: Relic[] = []
            const relicInformation: Relic[] = JSON.parse(
                JSON.stringify(relics.value)
            )

            for (let i in obj) {
                for (let i2 of relicInformation) {
                    if (i2.jaName === i) {
                        i2.count = obj[i]
                        relicsDetails.push(i2)
                    }
                }
            }
            return relicsDetails
        }

        const calculateRemainder = (
            nes: Counter,
            bel: Counter
        ): { remainder: Counter; lack: Counter } => {
            const diff = Object.entries(nes).reduce(
                (acc, [key, value]) => {
                    return { ...acc, [key]: (acc[key] || 0) - value }
                },
                { ...bel } as Partial<Counter>
            ) as Counter

            let remainder: Counter = {}
            let lack: Counter = {}

            for (let i in diff) {
                if (diff[i] > 0) {
                    remainder = { ...remainder, [i]: diff[i] }
                } else if (diff[i] < 0) {
                    lack = { ...lack, [i]: Math.abs(diff[i]) }
                }
            }
            return {
                remainder: remainder,
                lack: lack,
            }
        }

        const unnecessaryRelics = computed(() => {
            if (!necessaryRelics.value.length) {
                return
            }

            let unnecessaryRelics = calculateRemainder(
                getRelics(necessaryRelics.value),
                getRelics(belongings.value)
            )

            while (Object.keys(getComponents(unnecessaryRelics.lack)).length) {
                unnecessaryRelics = calculateRemainder(
                    getComponents(unnecessaryRelics.lack),
                    unnecessaryRelics.remainder
                )
            }
            return unnecessaryRelics.remainder
        })

        const test = (nes: Counter, bel: Counter) => {
            let totalDiscount = 0
            for (let nesRelic in nes) {
                for (let belRelic in bel) {
                    if (!(nesRelic === belRelic)) {
                        continue
                    }
                    const relic = getRelicDetails(nes).find(
                        (r) => r.jaName === nesRelic
                    ) as Relic

                    if (nes[nesRelic] >= bel[belRelic]) {
                        totalDiscount += relic.totalPrice * bel[belRelic]
                        nes[nesRelic] -= bel[belRelic]
                    } else if (nes[nesRelic] <= bel[belRelic]) {
                        totalDiscount += relic.totalPrice * nes[nesRelic]
                        nes[nesRelic] -= nes[nesRelic]
                    }

                    if (nes[nesRelic] === 0) {
                        delete nes[nesRelic]
                    }
                }
            }
            return { nes, totalDiscount }
        }

        const totalCost = computed(() => {
            let nesTotal = 0

            necessaryRelics.value.filter((nes) => {
                nesTotal += nes.totalPrice * nes.count
            })

            let obj = test(
                getRelics(necessaryRelics.value),
                getRelics(belongings.value)
            )

            nesTotal -= obj.totalDiscount

            while (Object.keys(getComponents(obj.nes)).length) {
                obj = test(getComponents(obj.nes), getRelics(belongings.value))
                nesTotal -= obj.totalDiscount
            }

            return nesTotal
        })

        axios
            .get('relic_calculator/relics')
            .then((response) => {
                relics.value = response.data
                isLoading.value = false
            })
            .catch((error) => {
                console.log(error.response)
            })

        return {
            relics,
            belongings,
            quality,
            searchWord,
            filteredRelics,
            filteredbelongings,
            addCount,
            subtractCount,
            necessaryRelics,
            filterednecessaryRelics,
            unnecessaryRelics,
            cloneRelic,
            totalCost,
            isLoading,
        }
    },
})
</script>
<style scoped>
.Common,
.Rare,
.Elite {
    display: inline-block;
}

.wrapper-box {
    display: flex;
}

.belongings {
    background: palegreen;
    width: 50%;
    height: 400px;
}
.necessary-relic {
    background: paleturquoise;
    width: 50%;
    height: 400px;
}
</style>
