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
                    <select class="form-select" v-model="select_file" id="select_label" v-on:change="function() {sheet_info = JSON.parse(JSON.stringify(xlsx_name[select_file][0]));}">
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
            <div style="overflow-y:scroll; height:70vh; overflow-x: hidden;" class="mt-5">
                <div class="row justify-content-center" v-for="(project, index) in project_info" :key="index" :vlaue="project">
                    <div class="col-xl-2 col-lg-2 col-md-2 col-xs-12 mt-5">
                        <h4>{{ index }}</h4>
                    </div>
                    <div class="col-xl-2 col-lg-2 col-md-2 col-xs-12">
                        <label for="question_one" class="form-label py-3">權重比(%)</label>
                        <input class="form-control" id="question_one_value" type="text" :value="String(project[0]*100)+'%'" readonly>
                    </div>
                    <div class="col-xl-2 col-lg-2 col-md-2 col-xs-12">
                        <label for="question_one" class="form-label py-3">總量</label>
                        <input class="form-control" id="question_one_value" type="text" :value="project[1]" readonly>
                    </div>
                    <div class="col-xl-2 col-lg-2 col-md-2 col-xs-12">
                        <label for="question_one" class="form-label py-3">完工量</label>
                        <input class="form-control" id="question_one_value" type="text" placeholder="完成量" v-model="project[2]">
                    </div>  
                    <div class="col-xl-2 col-lg-2 col-md-2 col-xs-12">
                        <label for="question_one" class="form-label py-3">完工率(%)</label>
                        <input class="form-control" id="question_one_value" type="text" :value="String((project[2]/project[1])*100)+'%'" readonly>
                    </div>    
                </div>
            </div>
            <center class="mt-5">
                <div class="row justify-content-center">
                    <div class="col-5">
                        <button type="button" class="btn btn-danger" style="padding:2vh 5vw">清除</button>
                    </div>
                    <div class="col-5">
                        <button type="button" class="btn btn-primary" style="padding:2vh 5vw" v-on:click="post_excel">確認</button>
                    </div>
                </div>
            </center>
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
            excel_date:'',
            select_file:'',
            select_sheet:'',
            xlsx_name:'',
            sheet_info:[],
            project_info:[],
        }
    },
    created:function(){  // 網頁載入時，一開始就載入
        this.excel_info()
    },
    methods:{
        excel_info:async function() { //取得excel相關資訊(權重、項目名稱等..)
            axios.get('/api/excel_read/').then(
                response => {
                    this.xlsx_name = response.data
                },
                error => {
                    alert(error)
                }
            )
        },

        post_excel:async function() {  //將使用者填表單資料送到後端
            let formData = new FormData;
            formData.append('select_date',this.excel_date)
            formData.append('select_loop',this.select_file)
            formData.append('select_plant',this.select_sheet)
            for (var i in this.project_info) {
                formData.append(i,[this.project_info[i][2],Number(this.project_info[i][2])/Number(this.project_info[i][1])*100])
            }
            console.log(formData)
            axios({ 
                method: 'post',
                url: '/api/excel_write/ ',
                xstfCookieName: 'csrftoken',
                xsrfHeaderName: 'X-CSRFToken',
                data: formData,
                responseType: 'json',
                headers: {
                    'X-CSRFToken': 'csrftoken',
                }
            }).then(response => console.log(response));
            window.alert('輸入成功')
        },

    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    header {
        height: auto;
    }
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
