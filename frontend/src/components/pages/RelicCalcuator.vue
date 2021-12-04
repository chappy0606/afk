<template>
    <div>
        <div class="quality-nav">
            <label><input type="radio" value="" v-model="quality" />All</label>
            <label><input type="radio" value="Common" v-model="quality" />Common</label>
            <label><input type="radio" value="Rare" v-model="quality" />Rare</label>
            <label><input type="radio" value="Elite" v-model="quality" />Elite</label>
        </div>

        <div class="relic-list">
            <draggable v-model="test" group="relic-list" item-key="id" handle=".handle" @update="onUpdate">
                <template #item="{element}">
                    <span class="handle">
                <img
                    :src="element.icon"
                    width="50"
                    height="50"
                    :alt="element.jaName"
                />
                    </span>
                </template>
        </draggable>
        </div>

        <div class="test-box">

        </div>

    </div>
</template>

<script lang="ts">
import { defineComponent, computed, ref } from 'vue'
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
    components:{
        draggable
    },
    setup() {
        const relics = ref<Relic[]>([])
        const quality = ref<string>('')

        axios
            .get('relic_calculator/relics')
            .then(response => {
                relics.value = response.data
            })
            .catch(error => {
                console.log(error.response)
            })

        const test = computed({set:() =>  {
            return
        },
        get: () => relics.value.filter(relic => 
            relic.quality.includes(quality.value))
        })

        const onUpdate = (originalEvent: { newDraggableIndex: number, oldDraggableIndex: number}) => {
            const tmp = relics.value[originalEvent.newDraggableIndex]
            relics.value[originalEvent.newDraggableIndex] = relics.value[originalEvent.oldDraggableIndex]
            relics.value[originalEvent.oldDraggableIndex] = tmp
        }
            
        return {
            test,
            quality,
            relics,
            onUpdate,
        }
    }
})
</script>
<style>
li {
    list-style: none;
    display: inline-block;
}

.test-box{
    width: 80px;
    height: 80px;
    background-color: red;
}

</style>
