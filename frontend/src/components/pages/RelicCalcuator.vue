
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

        const cloneRelic = (value:Relic) => {
            return {id: value.id,
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
                count: value.count
            }
        }

        const countDuplicates = (array:string[]) :Counter => {
            return array.filter(Boolean).reduce((prev,current) => {
                prev[current] = (prev[current] || 0) + 1
                return prev
                },{} as Partial<Counter>) as Counter
        }

        const getRelics = (array:Relic[]) :Counter => {
            const relics:string[] = []
            array.filter(relic=> {
                    for(let i = 0; i < relic.count; i++){
                        relics.push(relic.jaName)
                    }
            })
            return countDuplicates(relics)
        }

        const getComponents = (array:Relic[]) :Counter => {
            const components:string[] = []
            array.filter(relic=> {
                for(let i = 0; i < relic.count; i++){
                    components.push(                        
                        relic.component1,
                        relic.component2,
                        relic.component3,
                        relic.component4)
                }
            })
            return countDuplicates(components)
        }

        const getRelicDetail = (obj:Counter) => {
            const relicsDetail:Relic[] = []
            const relicsDetail2:Relic[] = []

            const start2 = performance.now();
            for(let i in obj){
                for(let i2 in relics.value){
                    if(relics.value[i2].jaName === i){
                        relicsDetail2.push(relics.value[i2])
                    }
                }
            }
            const end2 = performance.now();
            console.log(end2 - start2);

            const start = performance.now();
            for(let i in obj){
                relics.value.filter(v=> {
                    if(v.jaName === i){
                        relicsDetail.push(v)
                    }
                })
            }
            const end = performance.now();
            console.log(end - start);
            return relicsDetail
        }

        const calculateRemainder = (nes:Counter,bel:Counter) :Counter => {
            const diff = Object.entries(nes).reduce((acc,[key,value]) => {
                return  ({ ...acc, [key]: (acc[key] || 0) - value })
            },{...bel} as Partial<Counter>) as Counter

            let remainder:Counter = {}

            for(let i in diff){
                if(diff[i] > 0){
                    remainder = {...remainder,[i]: diff[i]}
                }
            } 
            return remainder
        }
        
        const toralCost = computed(() => {
            let belongingsPrice: number = 0

            //作りたいものと所持品を比べて１以上の物をピックアップ(余り)
            const a = calculateRemainder(
                getRelics(necessaryRelics.value),
                getRelics(belongings.value)
            )
            //この時点で差がなければreturn
            // if(!Object.keys(a).length){
            //     console.log('return')
            //     return belongingsPrice
            // }

            //作りたいもののcomponetとピックアップされた所持品を比べる
            const b = calculateRemainder(
                getComponents(necessaryRelics.value), a
            )
            console.log(b)
            //作りたいもののcomponentのcomponentと現在の所持品比べる
            console.log(getRelicDetail(getComponents(necessaryRelics.value)))
            



            // let nesTotal = 0
            // necessaryRelics.value.filter(relic=> nesTotal += relic.totalPrice * relic.count)
            // let belTotal = 0
            // belongings.value.filter(relic=> belTotal+= relic.totalPrice * relic.count)

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
