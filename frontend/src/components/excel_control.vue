<template>
    <header class="masthead">
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-4">
                    <label for="date_select" class="form-label py-3">日期選擇</label>
                    <input class="form-control" id="date_select" type="date" v-model="excel_date" placeholder="完成量" aria-label="default input example">
                </div>
                <div class="col-4">
                    <label for="select_label" class="form-label py-3">迴路選擇</label>
                    <select class="form-select" v-model="select_file" id="select_label" aria-label="Default select example">
                        <option value="1-1" selected>1-1</option>
                        <option value="1-2">1-2</option>
                        <option value="1-3">1-3</option>
                        <option value="1-4">1-4</option>
                    </select>
                </div>
                <div class="col-4">
                    <label for="select_label" class="form-label py-3">廠區選擇</label>
                    <select class="form-select" v-model="select_sheet" id="select_label" aria-label="Default select example">
                        <option value="1-1" selected>1-1</option>
                        <option value="1-2">1-2</option>
                        <option value="1-3">1-3</option>
                        <option value="1-4">1-4</option>
                    </select>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-2 mt-5">
                    <h2>1. 點井施做</h2>
                </div>
                <div class="col-2">
                    <label for="question_one" class="form-label py-3">權重比(%)</label>
                    <input class="form-control" id="question_one_value" type="text" v-model="question_one_value" placeholder="完成量" aria-label="default input example" readonly>
                </div>
                <div class="col-2">
                    <label for="question_one" class="form-label py-3">總量</label>
                    <input class="form-control" id="question_one_value" type="text" v-model="question_one_value" placeholder="完成量" aria-label="default input example" readonly>
                </div>
                <div class="col-2">
                    <label for="question_one" class="form-label py-3">完工量</label>
                    <input class="form-control" id="question_one_value" type="text" v-model="question_one_value" placeholder="完成量" aria-label="default input example">
                </div>  
                <div class="col-2">
                    <label for="question_one" class="form-label py-3">完工率(%)</label>
                    <input class="form-control" id="question_one_value" type="text" v-model="question_one_value" placeholder="完成量" aria-label="default input example" readonly>
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
            select_file:'1-1',
            select_sheet:'1-1',
        }
    },
    created:function(){  // 網頁載入時，一開始就載入
        this.get_excel()
    },
    methods:{
        get_excel:async function() {
            axios.get('/api/excel_read/').then(
                response => {
                    this.abc = response.data
                },
                error => {
                    alert(error)
                }
            )
        },
        post_excel:async function() {
            // let formData = new FormData()
            // formData.append('question_one_value',this.question_one_value)
            // formData.append('question_one_percent',this.question_one_percent)
            // formData.append('question_two_value',this.question_two_value)
            // formData.append('question_two_percent',this.question_two_percent)
            // formData.append('sheet',this.sheet)
            // formData.append('excel_date',this.excel_date)

            // axios({
            //     method: 'post',
            //     url: '/api/excel_write/ ',
            //     xstfCookieName: 'csrftoken',
            //     xsrfHeaderName: 'X-CSRFToken',
            //     data: formData,
            //     headers: {
            //         'X-CSRFToken': 'csrftoken',
            //     }
            // }).then(response => console.log(response));
            window.alert('輸入成功')
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h2 {
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
