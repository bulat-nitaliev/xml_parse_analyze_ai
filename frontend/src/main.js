import { createApp } from 'vue'
import App from './App.vue'
import components from '@/components/UI'
import router from '@/router'
import store from '@/store'
import 'materialize-css/dist/css/materialize.min.css'
// import 'materialize/css/materialize.min.css'
// import 'materialize-css/dist/css/materialize.min.css'
// import 'material-design-icons/iconfont/material-icons.css'

const app = createApp(App)

router.beforeEach((to, from, next)=>{
    if(to.matched.some(record=>record.meta.requiresLogin)){
        if (!store.state.isAuth){
            next('/login')
        }else{
            next()
        }
    }else{
        next()
    }
})

components.forEach(component=>{
    app.component(component.name, component)
})
app.use(router).use(store).mount('#app')
