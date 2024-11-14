<template>
    <div class="select" @click.stop="showOption">
        <div class="title">{{optionSelect}} </div>
        <div class="option-wrapper" v-if="isVisibleOption">
            <div class="option"      
            :value="modelValue"           
            @click.stop="toggleOption(option)"
            v-for="option in options"
            :key="option.name"        
            >
            <span >{{option.name}}</span>
        </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'my-select',
    props: {
        options: {
            type: Array,
            required: true,
            default: []
        },
        modelValue: String,
        
    },
    data(){
        return {
           optionSelect: null, 
           isVisibleOption: false,
        }
    },
    methods: {
        toggleOption(option){
            this.optionSelect = option.name
            this.isVisibleOption = false
            this.$emit('update:modelValue', option)
        },
        showOption(){
            this.isVisibleOption = true   
        }
    },
    created() {
      window.addEventListener('click', (e) => {
        if (!this.$el.contains(e.target)){
          this.isVisibleOption  = false
        }
      })
  },
}
</script>

<style scoped>
.select {
    padding: 15px;
    cursor: pointer;
}
.title:hover {
    background: rgb(184, 228, 213);
}
.title {
    border: 1px solid teal;
    
    padding: 5px 25px;
    border-radius: 8px;
}
.option {
    display: flex;
    border: 1px solid teal;    
    padding: 5px 25px;
    border-radius: 8px;
    
    text-align: center;
}
.option:hover {
    background: rgb(184, 228, 213);
}
</style>