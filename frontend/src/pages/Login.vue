<template>
    <div>
        <main class="form-signin">
            <form 
            @submit.prevent="login">
               
                <h1 class="title">Please sign in</h1>
                <!-- <p v-if="!isAuth">вы не авторизованы</p> -->

                <div class="form-floating">
                <input 
                    v-model="username"
                    type="text" 
                    class="form-control"  placeholder="username">
                
                </div>
                <div class="form-floating">
                <input 
                    v-model="password"
                    type="password" 
                    class="form-control"  placeholder="Password">
                
                </div>

                <my-button >Sign in</my-button>
            </form>
        </main>
        <my-dialog v-model:show="isVisible">{{text}}</my-dialog>
    </div>
    
    
</template>

<script>
import {mapState, mapActions, mapMutations } from 'vuex'
export default {
    data:() => {
        return{
            username: '',
            password: '',
            
        }
    },
    computed: {
        ...mapState({
            isAuth: state=> state.isAuth,
            isVisible: state=> state.isVisible,
            text: state=> state.text,
        })
    },
    methods: { 
        
        login(){
            this.$store.dispatch('userLogin', 
            {
                username: this.username,
                password: this.password,
            }
            )
            .then((res)=>{
                this.$router.push('/')
            })
            .catch(err=>{
                this.isVisible = err
                this.isVisible = true
            })
        },

    }
    
}
</script>

<style scoped>
.form-signin {
  max-width: 330px;
  padding: 1rem;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-control {
    padding: 13px;
    margin-top: 10px;
    border: 1px solid teal;
}

.title {
    color: rgba(12, 38, 85, 0.856)
}
</style>