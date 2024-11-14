<template>  
  <div>
    <navbar></navbar>
    <div class="app">
      
        <h4 v-if="isAuth">Пользователь {{ name }} авторизован</h4>
        <h4 v-else>Авторизуйтесь</h4>
        <router-view></router-view>
    </div>
  </div>
     
</template>

<script>
import M from 'materialize-css'
import Navbar from './components/UI/Navbar.vue'
import {mapState, mapActions} from 'vuex'

export default {
  data: () => {
    return {
      name: localStorage.getItem('name')
    }
  },
  components: { Navbar },
  methods: {
    ...mapActions({
      chekAuth: 'chekAuth'
    }),
  },
  computed: {
    ...mapState({
      isAuth: state=> state.isAuth
    })
  },
  created(){
    if (localStorage.getItem('token')){
      this.chekAuth()
    }
    
  },
  mounted(){
    M.AutoInit()
  
  }
  
  
}
</script>

<style>
* {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    .app {
        padding: 20px;
    }


</style>
