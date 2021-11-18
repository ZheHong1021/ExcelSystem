<template>
    <header class="masthead">
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-5">
                    <label for="question_one" class="form-label py-3">點井施作</label>
                    <input class="form-control" id="question_one_value" type="text" v-model="question_one_value" placeholder="完成量" aria-label="default input example">
                </div>
                <div class="col-5">
                    <label for="question_onetoone" class="form-label py-3">點井施作</label>
                    <input class="form-control" id="question_one_percent" type="text" v-model="question_one_percent" placeholder="完成率" aria-label="default input example">
                </div>
                <div class="col-5">
                    <label for="question_two" class="form-label py-3">放樣（集汚池及圓池）</label>
                    <input class="form-control" id="question_two_value" type="text" v-model="question_two_value" placeholder="完成量" aria-label="default input example">
                </div>   
                <div class="col-5">
                    <label for="question_twototwo" class="form-label py-3">放樣（集汚池及圓池）</label>
                    <input class="form-control" id="question_two_percent" type="text" v-model="question_two_percent" placeholder="完成率" aria-label="default input example">
                </div>   
                <div class="col-5">
                    <center><button type="button" class="clear py-3 px-5 btn-block">清除</button></center>
                </div>
                <div class="col-5">
                    <center><button type="button" class="check py-3 px-5 btn-block" v-on:click="post_excel">確認</button></center>
                </div>        
            </div>
            <a href="./E向陽多元-S01-2021.11.05 (養殖)-h.xlsx" download>下載</a>
        </div>
    </header>
</template>

<script>
//import * as Excel from '../services/input_excel.js';
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
export default {
    data(){
        return{
            question_one_value:null,
            question_one_percent:null,
            question_two_value:null,
            question_two_percent:null,
            case:[]
        }
    },
    created:function(){  // 網頁載入時，一開始就載入
        
    },
    methods:{
        post_excel:async function() {
            let formData = new FormData()
            formData.append('question_one_value',this.question_one_value)
            formData.append('question_one_percent',this.question_one_percent)
            formData.append('question_two_value',this.question_two_value)
            formData.append('question_two_percent',this.question_two_percent)

            axios({
                    method: 'post',
                    url: '/api/excel_write/',
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    data: formData,
                    headers: {
                        'X-CSRFToken': 'csrftoken',
                    }
                }).then(response => console.log(response));
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    label {
        color: white;
        font-weight: 1000;
    }
    .check {
        background-color:#2894FF;
        border-radius:5px;
    }
    .clear {
        background-color:#EA0000;
        border-radius:5px;
    }
    input {
        width: 100%;
    }
</style>
