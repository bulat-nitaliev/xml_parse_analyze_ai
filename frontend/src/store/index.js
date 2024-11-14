
import { createStore } from 'vuex'
import AuthService from '@/services/AuthService'
import axios from 'axios'
import { API_URL } from '@/http'
// import {prof} from '@/store/prof'


export default createStore({
  state: {
    isVisible: false,
    text: '',
    isAuth: false,
  },
  getters: {
    logedIn(state){
      return state.accesToken != null
    }
  },
  mutations: {
    setVisible(state, bool){
      state.isVisible = bool
    },
    
    setAuth(state, bool){
      state.isAuth = bool
    },
    setText(state, text){
      state.text = text
    },
   
    destroyToken(state){
      state.accesToken = null
      state.refreshToken = null
    }
  },
  actions: {
    async userLogin(context,userObject){     
        try {
          const response = await AuthService.login(userObject.username, userObject.password)
          if (response.code !== 200){
            
            console.log(response.status);
          }
          localStorage.setItem('token', response.data.access) 
          localStorage.setItem('refresh', response.data.refresh) 
          localStorage.setItem('name', response.data.username) 
          context.commit('setAuth', true) 
          M.toast({html: 'Успешно ' , classes: 'rounded teal '})
        } catch (error) {
          M.toast({html: 'Не правильно введен логин или пароль попробуйте снова', classes: 'rounded teal '})
          // context.commit('setVisible', true)
          // context.commit('setText', "Не правильно введен логин или пароль попробуйте снова")
          console.log(response.code);
        }
            
        //     context.commit('setAuth', true)
        // return new Promise((resolve, reject)=>{
        //   AuthService.login(userObject.username, userObject.password)
        //   .then(response=>{
        //     localStorage.setItem('token', response.data.access)           
        //     context.commit('setAuth', true)  
        //   resolve()
        //   })        
        // })         
    },
    async userRegister(context, userObject){
      
        try {
          const response = await AuthService.register(
            userObject.username, userObject.password, userObject.email, 
            userObject.first_name, userObject.last_name)
            M.toast({html: 'Успешно зарагистрирован пользователь' , classes: 'rounded teal '})
          // localStorage.setItem('token', response.data.accessToken)
          // context.commit('isAuth', true)
          console.log(response.data);
        } catch (error) {
          console.log(error);
          M.toast({html: 'Не корректные данные попробуйте снова', classes: 'rounded teal '})
        }
      
        
    },
    // userLogin(context, usercredentials){
    //   return new Promise((resolve, reject)=> {
    //     getApi.post('/api/token/', {
    //       username:usercredentials.username,
    //       password: usercredentials.password
    //     })
    //     .then(res=>{
    //       context.commit('updateStorage', {access: res.data.access, refresh: res.data.refresh})
    //       resolve()
    //     })
    //   })
    // },
    userLogout(context){
      if(context.state.isAuth){
        context.commit('setAuth', false)
        localStorage.removeItem('token')
        localStorage.removeItem('refresh')
        localStorage.removeItem('name')
      }
    },
    async chekAuth(context){
      try {
        const response = await axios.post(`${API_URL}/api/token/refresh/`, {
          withCredentials: true, 
          refresh: localStorage.getItem('refresh')
        })
        localStorage.setItem('token', response.data.access) 
        
        context.commit('setAuth', true) 
      } catch (error) {
        console.log(error)
      }
      
    }
  },
  
  
})
