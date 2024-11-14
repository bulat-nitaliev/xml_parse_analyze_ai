<template>
    <div class="form-signin">
        <form @submit.prevent="register"> 
            <h1 class="title">Пожалуйста зарегистрируйтесь</h1>  
            <div class="form-floating">
                <input v-model="username" type="text" class="form-control" placeholder="username">
            </div>
            <div class="form-floating">
                <input v-model="password" type="password" class="form-control" placeholder="password">
            </div>
            <div class="form-floating">
                <input v-model="email" type="email" class="form-control" placeholder="email">
            </div>
            <div class="form-floating">
                <input v-model="first_name" type="text" class="form-control" placeholder="first_name">
            </div>
            <div class="form-floating">
                <input v-model="last_name" type="text" class="form-control" placeholder="last_name">
            </div>
            
            <my-button >registration</my-button>
        </form>
    </div>
    
</template>

<script>

export default {
  
  data:()=>{
    return {
        username: '',
        password: '',
        email: '',
        first_name: '',
        last_name: '',
    }
  },
  methods: {
    register(){
            this.$store.dispatch('userRegister', 
            {
                username: this.username,
                password: this.password,
                email: this.email,
                first_name: this.first_name,
                last_name: this.last_name
            }
            ).then(res=>{
                this.$router.push('/login')
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