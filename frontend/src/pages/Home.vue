<template>
    <div>
        <!-- <my-button @click="userList">Получить список пользователей</my-button>
        <div v-for="user in list_users" :key="user.id">
            <div>{{ user.first_name}}</div>
            <div>{{ user.last_name}}</div>
            <div>{{user.email}}</div>
            <br>
        </div> -->
        <div class="row">
            <div class="col s3"><input v-model="path1" type="text" name="" id="" placeholder="Укажите полный путь к файлу xml">
                <button class="btn small" v-on:click="parser">Add database</button>
            </div>
            <div class="col s3">
                <input v-model="date_product" type="date" name="" id="" placeholder="Укажите дату для полученя отчета по продуктам">
                <button class="btn small" v-on:click="report(date_product)">Get Report</button>
            </div>
            
            <div class="col s3"></div>
        </div>
        <div class="row">
            <form class="col s12">
            <div class="row">
                
                <div class="input-field col s12">
                    
                <textarea v-model="prompt" id="textarea1" class="materialize-textarea" placeholder="Укажите промпт с указанием результатов отчета для получения ответа от GigaChat"></textarea>
                <!-- <label for="textarea1">Пример: Составь краткий аналитический отчет с выводами и рекомендациями</label> -->
                </div>
                <button class="btn small" v-on:click="prompt_ai(prompt)">Get Answer</button>
                <label style="margin-left: 20px;">Пример: Составь краткий аналитический отчет с выводами и рекомендациями</label>
            </div>
            </form>
        </div>
        

        <my-dialog v-model:show="isDialog" style="white-space: pre-wrap;">
        <h5 style="color: teal">{{ message }}  </h5>
        </my-dialog>

        <my-loader v-if="isLoader"></my-loader>

        <div class="container" v-if="Object.keys(list_report).length > 0">
            <div class="row">
                <div class="col s4">
                    <div><strong>total_revenue</strong></div>
                    <div style="margin-top: 20px;">{{ list_report.total_revenue.join() }}</div>   
                </div>
                <div class="col s4">
                    <div><strong>categories</strong> </div>
                    <div style="margin-top: 20px;" v-for="cat in list_report.categories">{{ cat.join() }}</div>
                    
                </div>
                <div class="col s4">
                    <div><strong>top_products</strong></div>
                    <div style="margin-top: 20px;"  v-for="prod in list_report.top_products">{{ prod.join() }}</div>
                </div>
                
            </div>
        </div>

        
        
    </div>
</template>

<script>
import UserService from '@/services/UserService'
import $api from '@/http';
export default {
    data: ()=>{
        return {
            list_report: {},
            path1: '',
            message: '',
            isDialog: false,
            isLoader: false,
            prompt: '',
            date_product: '',
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
    },
    async parser(){
        try {
            this.isLoader = true
            let newPath = this.path1.replace(/\\/g, '\\\\')
            console.log(newPath);
            
            const response = await $api.post('/api/parse_xml/', {'path': newPath})
            this.isLoader = false

            this.message = response.data.res
            this.isDialog = true
            this.path1 = ''
        } catch (error) {
            console.log(error);
        }
    },
    async report(dt){
        try {
            this.isLoader = true
            const response = await $api.post('/api/report/', {'date_product': dt})
            
            this.isLoader = false
            this.list_report = response.data
            console.log(this.list_report);
            
            
        } catch (error) {
            console.log(error);
            this.message = error
            this.isDialog = true
            this.isLoader = false
        }
    }, 
    async prompt_ai(prompt){
        try {
            this.isLoader = true
            const response = await $api.post('/api/analytical_report/', {'prompt': prompt})
            
            this.isLoader = false
            this.message = response.data.res
            console.log(this.message);
            
            this.isDialog = true
            
        } catch (error) {
            console.log(error);
            this.message = error
            this.isDialog = true
            this.isLoader = false
        }
    }, 
   } 

}
</script>

<style scoped>

</style>