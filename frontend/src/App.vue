<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <button type="button" v-on:click="get_json">click</button>
    {{ abc }}
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export default {
    data() {
        return{
            abc:'',
        }
    },
    name: 'App',
    components: {
        HelloWorld
    },
    methods: {
        get_json() {
            let formData = new FormData()
            formData.append('132','123')
            // axios.get('/api/test/').then(
            //     response => {
            //         this.abc = response.data
            //     },
            //     error => {
            //         alert(error)
            //     }
            // )
            axios({
                method: 'post',
                url: 'api/test/',
                xstfCookieName: 'csrftoken',
                xsrfHeaderName: 'X-CSRFToken',
                data: formData,
                headers: {
                    'X-CSRFToken': 'csrftoken',
                },
            }).then(response => console.log(response));
        }
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
