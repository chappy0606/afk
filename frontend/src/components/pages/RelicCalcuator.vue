<template>
    <div>
        <div class="quality-nav">
            <label><input type="radio" value="" v-model="quality" />all</label>
            <label><input type="radio" value="Common" v-model="quality" />Common</label>
            <label><input type="radio" value="Rare" v-model="quality" />Rare</label>
            <label><input type="radio" value="Elite" v-model="quality" />Elite</label>
            <input type="text" v-model="searchWord" />
        </div>

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

            <div class="test">
            <div class="belongings">
            <draggable
                v-model="filteredbelongings"
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
                            <div>
                            <label>{{ element.count }}</label>
                            <button id="belongings-add-btn" @click="addCount($event, index)">+</button>
                            <button id="belongings-sub-btn" @click="subtractCount($event, index)">-</button>
                            </div>
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
                            <button id="necessary-relic-add-btn" @click="addCount($event, index)">+</button>
                            <button id="necessary-relic-sub-btn" @click="subtractCount($event, index)">-</button>
                        </span>
                    </div>
                </template>
            </draggable>
            </div>
        </div>
        必要コスト:{{sumArray}}
    </div>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue'
import { component } from 'vue/types/umd'
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
    count: number | undefined
}

export default defineComponent({
    components: {
        draggable
    },
    setup() {
        const relics = ref<Relic[]>([])
        const belongings = ref<Relic[]>([])
        const necessaryRelics = ref<Relic[]>([])
        const quality = ref<string>('')
        const searchWord = ref<string>('')

        const filteredRelics = computed({
            get: () => {
                return relics.value
                    .filter(relic => {
                        return (
                            relic.enName
                                .toUpperCase()
                                .includes(searchWord.value.toUpperCase()) ||
                            relic.jaName.includes(searchWord.value)
                        )
                    })
                    .filter(relic => relic.quality.includes(quality.value))
            },
            set: value => (relics.value = value)
        })

        const filterRelics = (array:Relic[])=> {
            return array
                .filter((x, i, self) => {
                    if (typeof x.count === 'undefined' || x.count <= 0) {
                        x.count = 1
                    }
                    return self.indexOf(x) === i
                })
                .sort((a, b) => Number(a.id) - Number(b.id))
        }

        const filteredbelongings = computed({
            get: () => belongings.value,
            set: value => belongings.value = filterRelics(value)
        })

        const filterednecessaryRelics = computed({
            get: () => necessaryRelics.value,
            set: value => necessaryRelics.value = filterRelics(value)
        })

        const addCount = (event:{target:HTMLInputElement}, index: number) => {
            if(event.target.id === 'belongings-add-btn'){
                belongings.value[index].count++
            }else{
                necessaryRelics.value[index].count++
            }
        }

        const removeRelic= (array:Relic[],index:number) =>{
            if(array[index].count <= 0){
                array.splice(index,1)
            }
        }

        const subtractCount = (event:{target:HTMLInputElement}, index: number) => {
            if(event.target.id === 'belongings-sub-btn'){
                belongings.value[index].count--
                removeRelic(belongings.value,index)
            }else{
                necessaryRelics.value[index].count--
                removeRelic(necessaryRelics.value,index)
            }
        }

        const test = ()=> {
            let comps: string[] = []
            necessaryRelics.value.filter(relic=> {
                for(let i = 0; i < relic.count; i++){
                comps.push(relic.compornent1)
                comps.push(relic.compornent2)
                comps.push(relic.compornent3)
                comps.push(relic.compornent4)
                }
            })
            const test2 = comps.filter(Boolean)
            console.log(test2)
            // test2 = [知恵の眼,知恵の眼]
            relics.value.filter((relic)=>{
                if(test2.find(value=> value === relic.jaName)){
                    // 知恵の石
                    console.log(relic.compornent1)
                }
            })
        }

        const sumArray = computed(() => {
            let belongingsPrice: number = 0
            let necessaryRelicsPrice: number = 0
            test()
            for (let i in belongings.value) {
                belongingsPrice +=
                    belongings.value[i].totalPrice * belongings.value[i].count
            }
            for (let i in necessaryRelics.value){
                necessaryRelicsPrice += necessaryRelics.value[i].totalPrice * necessaryRelics.value[i].count
            }
            return necessaryRelicsPrice - belongingsPrice
        })

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
            filteredbelongings,
            addCount,
            subtractCount,
            necessaryRelics,
            filterednecessaryRelics,
            sumArray
        }
    }
})
</script>
<style>

.Common, .Rare, .Elite   {
    display: inline-block;
}

.test {
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
