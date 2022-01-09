
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
                :clone="cloneRelic"
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
                            <label>{{ element.count }}</label>
                            <button id="belongings-add-btn" @click="addCount($event, index)">+</button>
                            <button id="belongings-sub-btn" @click="subtractCount($event, index)">-</button>
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
        必要コスト:{{toralCost}}
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
    count: number
}
interface Counter {
    [key:string]: number
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
                                .toLowerCase()
                                .includes(searchWord.value.toLowerCase()) ||
                            relic.jaName.includes(searchWord.value)
                        )
                    })
                    .filter(relic => relic.quality.includes(quality.value))
            },
            set: value => relics.value = value
            })

        const filterRelics = (array:Relic[])=> {
            return array
                .filter((relic, index, array) => {
                    if (typeof relic.count === 'undefined' || relic.count <= 0) {
                        relic.count = 1
                    }
                    return array.findIndex(v => relic.id === v.id) === index
                })
                .sort((a, b) => Number(a.id) - Number(b.id))
        }

        const filteredbelongings = computed({
            get: () => {
                return belongings.value},
            set: value => {
                return belongings.value = filterRelics(value)}
        })

        const filterednecessaryRelics = computed({
            get: () => necessaryRelics.value,
            set: value => necessaryRelics.value = filterRelics(value)
        })

        const removeRelic= (array:Relic[],index:number) :void =>{
            if(array[index].count <= 0){
                array.splice(index,1)
            }      
        }

        const addCount = (event:{target:HTMLInputElement}, index: number) :void => {
            if(event.target.id === 'belongings-add-btn'){
                belongings.value[index].count++
            }else if(event.target.id === 'necessary-relic-add-btn'){
                necessaryRelics.value[index].count++
            }
        }

        const subtractCount = (event:{target:HTMLInputElement}, index: number) :void => {
            if(event.target.id === 'belongings-sub-btn'){
                belongings.value[index].count--
                removeRelic(belongings.value,index)
            }else if(event.target.id === 'necessary-relic-sub-btn'){
                necessaryRelics.value[index].count--
                removeRelic(necessaryRelics.value,index)
            }
        }

        const reduceQuality = (array:Relic[]) :Counter => {
            const compornents: string[] = []
            
            array.filter(relic=> {
                if(!relic.compornent1){
                    for(let i = 0; i < relic.count; i++){
                        compornents.push(relic.jaName)
                    }
                }else{
                    for(let i = 0; i < relic.count; i++){
                        compornents.push(                        
                            relic.compornent1,
                            relic.compornent2,
                            relic.compornent3,
                            relic.compornent4)
                    }
                }
            })

            const countDuplicate = (array:string[]) => {
                return array.filter(Boolean).reduce((prev,current) => {
                    prev[current] = (prev[current] || 0) + 1
                    return prev
                    },{} as Partial<Counter>) as Counter
            }

            const obj = countDuplicate(compornents)
            let result:string[] = []

            relics.value.filter(relic =>{
                for(let key of Object.keys(obj)){
                    if(relic.jaName.includes(key) && !relic.compornent1){
                        for(let i = 0; i < obj[key as keyof Counter]; i++){
                            result.push(relic.jaName)
                        }
                        break
                    }
                    if(relic.jaName.includes(key)){
                        for(let i = 0; i < obj[key as keyof Counter]; i++){
                            result.push(
                                relic.compornent1,
                                relic.compornent2,
                                relic.compornent3,
                                relic.compornent4,
                            )
                        }
                    }
                }
            })
            return countDuplicate(result)
        }

        const cloneRelic = (value:Relic) => {
            return {id: value.id,
                enName: value.enName,
                jaName: value.jaName,
                quality: value.quality,
                compornent1: value.compornent1,
                compornent2: value.compornent2,
                compornent3: value.compornent3,
                compornent4: value.compornent4,
                cost: value.cost,
                totalPrice: value.totalPrice,
                icon: value.icon,
                count: value.count
            }
        }
        
        const toralCost = computed(() => {
            const nes = reduceQuality(necessaryRelics.value)
            const bel = reduceQuality(belongings.value)

            const marged = Object.entries(nes).reduce((acc,[key,value]) => {
                console.log(acc[key])
                return  ({ ...acc, [key]: (acc[key] || 0) - value })
            },{...bel} as Partial<Counter>) as Counter
            
            console.log(marged)

            let belongingsPrice: number = 0

            return belongingsPrice
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
            toralCost,
            cloneRelic
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
