class Relic {
    id?: string
    name?: string
    quality?: string
    compornents?: {
        compornent: string
        num: number
    }[]
    cost?: number
    totalPrice?: number

    constructor(init: Partial<Relic>) {
        Object.assign(this, init)
    }
}

// apiで取得よていの形
const response = [
    {
        compornent: 'aaa',
        num: 1
    },
    {
        compornent: 'bbb',
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
