import axios from 'axios'

// const instanse = axios.create()

axios.interceptors.response.use((response) => {
    console.log('eeeeeeeeeeeeeeeee')
    return response
},
error => {
    console.log(error);
})

export default axios