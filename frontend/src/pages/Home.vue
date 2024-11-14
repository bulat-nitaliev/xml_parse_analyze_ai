<template>
    <div>
        <my-button @click="userList">Получить список пользователей</my-button>
        <div v-for="user in list_users" :key="user.id">
            <div>{{ user.first_name}}</div>
            <div>{{ user.last_name}}</div>
            <div>{{user.email}}</div>
            <br>
        </div>
    </div>
</template>

<script>
import UserService from '@/services/UserService'
export default {
    data: ()=>{
        return {
            list_users: []
        }
    },
   methods:{
    async userList(){
        try {
            const response = await UserService.fetchUsers()
            this.list_users = response.data["results"]
        } catch (error) {
            console.log(error);
        }
    }
   } 

}
</script>

<style scoped>

</style>