<template>
    <header class="masthead">
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-4">
                    <label for="date_select" class="form-label py-3">日期選擇</label>
                    <input class="form-control" id="date_select" type="date" v-model="excel_date" placeholder="完成量">
                </div>
                <div class="col-4">
                    <label for="select_label" class="form-label py-3">迴路選擇</label>
                    <select class="form-select" v-model="select_file" id="select_label" v-on:change="get_excel">
                        <option v-for="(xlsx, index) in xlsx_name" :key="index">{{ index }}</option>
                    </select>
                </div>
                <div class="col-4">
                    <label for="select_label" class="form-label py-3">廠區選擇</label>
                    <select class="form-select" v-model="select_sheet" id="select_label" v-on:change="function() {project_info = JSON.parse(JSON.stringify(xlsx_name[select_file][1]));}">
                        <option v-for="(file, index) in sheet_info" :key="index" :vlaue="file">{{ file }}</option>
                    </select>
                </div>
            </div>
            <div class="row justify-content-center" v-for="(project, index) in project_info" :key="index" :vlaue="project">
                <div class="col-2 mt-5">
                    <h4>{{ index }}</h4>
                </div>
                <div class="col-2">
                    <label for="question_one" class="form-label py-3">權重比(%)</label>
                    <input class="form-control" id="question_one_value" type="text" placeholder="完成量" aria-label="default input example" :value="String(project[0]*100)+'%'" readonly>
                </div>
                <div class="col-2">
                    <label for="question_one" class="form-label py-3">總量</label>
                    <input class="form-control" id="question_one_value" type="text" placeholder="完成量" aria-label="default input example" :value="project[1]" readonly>
                </div>
                <div class="col-2">
                    <label for="question_one" class="form-label py-3">完工量</label>
                    <input class="form-control" id="question_one_value" type="text" placeholder="完成量" v-model="project[2]" aria-label="default input example">
                </div>  
                <div class="col-2">
                    <label for="question_one" class="form-label py-3">完工率(%)</label>
                    <input class="form-control" id="question_one_value" type="text" placeholder="完成量" :value="String((project[2]/project[1])*100)+'%'" aria-label="default input example" readonly>
                </div>     
            </div>
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
            data_json: new FormData(),
            excel_date:'',
            select_file:'',
            select_sheet:'',
            xlsx_name:"",
            sheet_info:[],
            project_info:[],
        }
    },
    created:function(){  // 網頁載入時，一開始就載入
        this.excel_info()
    },
    methods:{
        excel_info:async function() {
            axios.get('/api/excel_read/').then(
                response => {
                    this.xlsx_name = response.data
                },
                error => {
                    alert(error)
                }
            )
        },
        get_excel:async function() {
            let formData = new FormData()
            formData.append('select_file',this.select_file)
            this.sheet_info = JSON.parse(JSON.stringify(this.xlsx_name[this.select_file][0]));
            // axios({
            //     method: 'post',
            //     url: '/api/excel_read/',
            //     xstfCookieName: 'csrftoken',
            //     xsrfHeaderName: 'X-CSRFToken',
            //     data: formData,
            //     headers: {
            //         'X-CSRFToken': 'csrftoken',
            //     }
            // }).then(response => console.log(response));
        },
        post_excel:async function() {
            let formData = new FormData()
            formData.append('question_one_value',this.question_one_value)
            formData.append('question_one_percent',this.question_one_percent)
            formData.append('question_two_value',this.question_two_value)
            formData.append('question_two_percent',this.question_two_percent)
            formData.append('sheet',this.sheet)
            formData.append('excel_date',this.excel_date)

            axios({
                method: 'post',
                url: '/api/excel_write/ ',
                xstfCookieName: 'csrftoken',
                xsrfHeaderName: 'X-CSRFToken',
                data: formData,
                headers: {
                    'X-CSRFToken': 'csrftoken',
                }
            }).then(response => console.log(response));
            window.alert('輸入成功')
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h4 {
        color: white;
    }
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
