const suuti: string = '3'


const test = (str:string) => {
    const suuti = str

    if (suuti.match('/^[0-9]*$/')) {
        return 1
    } else {
        return 0
    }
}

console.log(test(suuti))