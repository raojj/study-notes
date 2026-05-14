import axios from 'axios'

const request = axios.create({
    baseURL: 'http://localhost:9090',
    timeout: 10000
})

request.interceptors.request.use(
    config => {
        return config
    },
    error => {
        return Promise.reject(error)
    }
)

request.interceptors.response.use(
    response => {
        return response.data
    },
    error => {
        console.error('请求失败:', error)
        console.error('状态码:', error.response?.status)
        console.error('后端返回:', error.response?.data)
        return Promise.reject(error)
    }
)

export default request
