class Relic {
    id?: string
    name?: string
    quality?: string
    compornents?: {
        name: string
        num: number
    }[]
    cost?: number
    totalPrice?: number

    constructor(init: Partial<Relic>) {
        Object.assign(this, init)
    }
}

const response = [
    {
        name: 'aaa',
        num: 1
    },
    {
        name: 'bbb',
        num: 1
    }
]

const obj = {
    id: '1',
    name: 'test',
    quality: 'rare',
    compornents: response,
    cost: 1000,
    toralPrice: 3000
}

const test = new Relic(obj)
console.log(obj)
