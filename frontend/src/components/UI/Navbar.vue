<template>
    <div class="navbar">        
        <div @click="$router.push('/')">Kapital</div>
        <div class="navbar__btns">
            <my-button v-if="isAuth" @click="$router.push('/room')" >Room</my-button>
            <my-button v-if="!isAuth" @click="$router.push('/login')" >Login</my-button>
            <my-button v-if="isAuth" @click="userLogout" >Logout</my-button>
            <my-button v-if="!isAuth" @click="$router.push('/registr')" >Register</my-button>
        </div>      
    </div>
</template>

<script>
import {mapState, mapActions } from 'vuex'
export default {
    computed: mapState(['isAuth']),
    methods: {
        // ...mapActions({
        //     userLogout: 'userLogout'
        // })
        userLogout(){
            this.$store.dispatch('userLogout')
            .then(res=>this.$router.push('/login'))
        }
        
            
        }
    
    
}
</script>

<style scoped>
.navbar {
    height: 50px;
    color: green;
    background: lightgray;
    box-shadow: 2px 2px 4px gray;
    display: flex;
    align-items: center;
    padding: 0 15px;
}
.navbar__btns {
    margin-left: auto;
}
</style>