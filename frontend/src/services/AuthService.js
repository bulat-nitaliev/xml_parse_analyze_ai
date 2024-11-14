import $api from "@/http";
import axios from 'axios'
// import {getApi} from '@/axios-api'

export default class AuthService {
    static async login(username, password){
        return $api.post('/api/token/', {username, password})
    }

    static async register(username, password, email, first_name, last_name){
        const url = 'http://localhost:8000/api/users/'
        return axios.post(url, {username, password, email, first_name, last_name})
        // return getApi.post('/api/users/', {username, password, email, first_name, last_name})
    }
}