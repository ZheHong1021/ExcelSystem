<template>
    <div class="d-flex flex-column align-center justify-center">

        <!-- 新增用 Dialog -->
        <ImportDialog :dialog="import_dialog" @close-dialog="import_dialog = false"
            @refresh_Excel_Info="excel_info"/>

        <!-- Floating Btn Dialog -->
        <!-- Dialog(用來當作錨點功用的介面) -->
        <v-dialog v-model="floatBtn_dialog" scrollable :width="dialog_width">
            <v-card>
                <!-- title -->
                <v-card-title class="text-h6 font-weight-bold light-blue darken-4 white--text">
                    跳轉到該施工項目
                    <v-btn icon class="ml-auto white--text row-pointer" @click="floatBtn_dialog = false">
                        <v-icon>close</v-icon>
                    </v-btn>
                </v-card-title>
                <v-divider></v-divider>
                <!-- Content -->
                <v-card-text style="height: 400px;">
                    <!-- Search Input -->
                    <v-text-field
                        v-model="search"
                        append-icon="mdi-magnify"
                        label="搜尋施工項目"
                        single-line
                        hide-details
                        class="my-4"
                        clearable
                    ></v-text-field>

                        <!-- 實現目的 → 關閉 dialog -->
                        <!-- data-table設定 fixed-header必須搭配 height -->
                        <v-data-table
                            height="300"
                            :headers="table_header"
                            :items="project_info"
                            class="elevation-1"
                            fixed-header
                            disable-pagination
                            hide-default-footer
                            @click:row="handleTableRowClick"
                            disable-sort
                            mobile-breakpoint="100"
                            :search="search">
                        </v-data-table>
                    </v-card-text>

                <v-divider></v-divider>

                <!-- footer Action -->
                <v-card-actions class="d-flex justify-end">
                    <v-btn color="deep-orange darken-1 ml-auto text-h6" text @click="floatBtn_dialog = false">關閉</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <!-- Floating Button -->
            <v-speed-dial v-if="Object.keys(project_info).length > 0"
                fixed v-model="fab"
                bottom right direction="top"
                transition="slide-y-reverse-transition"
                >
                <template v-slot:activator>
                    <v-btn v-model="fab" color="deep-orange darken-1" dark fab>
                    <v-icon v-if="fab">mdi-close</v-icon>
                    <v-icon v-else>mdi-account-circle</v-icon>
                    </v-btn>
                </template>

                <v-btn fab dark small color="blue darken-2">
                    <!-- 資料填入的錨點 -->
                    <a href="javascript:void(0)" @click="goAnchor('top')" class="white--text">
                        <v-icon>arrow_upward</v-icon>
                    </a>
                </v-btn>
                <v-btn fab dark small color="green" @click="floatBtn_dialog = true">
                    <v-icon>search</v-icon>
                </v-btn>
            </v-speed-dial>

        <!-- 使用者選擇 -->
        <v-card :width="rwd_width"  class="mt-4 pa-8" >
            <v-row class="d-flex align-center">
                <v-col>
                    <v-chip color="green darken-2" class="white--text mb-4 font-weight-bold" label>
                        <v-icon left color="white">fact_check</v-icon>
                        使用者選擇
                    </v-chip>
                </v-col>

                <v-col class="text-right">
                    <v-btn class="ml-auto"  color="error" @click="import_dialog = true">
                        <v-icon left dense>note_add</v-icon>
                        匯入新報表
                    </v-btn>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" sm="6" md="4">
                    <label for="date_select" class="subtitle-1 font-weight-bold deep-orange--text">日期選擇</label>
                    <v-menu
                        v-model="date_menu"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        min-width="auto">
                            <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                v-model="date"
                                label="請選擇欲紀錄日期"
                                prepend-icon="mdi-calendar"
                                readonly
                                v-bind="attrs"
                                v-on="on"
                            ></v-text-field>
                        </template>

                        <v-date-picker
                            locale="zh-tw"
                            v-model="date"
                            @input="date_menu = false"
                            @change="changeDatePicker"
                        ></v-date-picker>
                    </v-menu>
                </v-col>

                <v-col cols="12" sm="6" md="4">
                    <label for="select_label" class="subtitle-1 font-weight-bold deep-orange--text">迴路選擇</label>
                    <v-select
                    v-on:change="change_File"
                        v-model="select_file"
                        :items="Object.keys(xlsx_name)"
                        label="迴路選擇..."
                        hide-details
                        prepend-icon="mdi-map"
                        single-line
                    ></v-select>
                </v-col>

                <v-col cols="12" sm="6" md="4">
                    <label for="select_label" class="subtitle-1 font-weight-bold deep-orange--text">廠區選擇</label>
                    <v-select
                        v-on:change="change_Sheet"
                        v-model="select_sheet"
                        :items="sheet_info"
                        label="廠區選擇..."
                        hide-details
                        prepend-icon="mdi-factory"
                        single-line
                        no-data-text = "請先選擇迴路"
                    ></v-select>
                </v-col>
            </v-row>
        </v-card>
        
        <!-- 資料填入 -->
        <Control 
            :project_info="project_info" 
            :xlsx_name="xlsx_name"
            @refresh="excel_info"
            @change_tab_show="show_submit_btn = true"
            @change_tab_close="show_submit_btn = false"
            @is_allow_save = "allow_save_method"/>

        <!-- 按鈕 (只有在工程進度時顯示) -->
        <div class="d-flex my-4" 
            v-if="Object.keys(project_info).length > 0 && show_submit_btn">

            <v-btn v-if="allow_save" 
                class="mx-4" x-large depressed color="primary" @click="post_excel">
                    <v-icon left>save</v-icon>
                    確定
            </v-btn>  

            <v-tooltip v-else  :value="showToolTip" top color="error">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                        class="mx-4" x-large depressed color="secondary"
                        v-bind="attrs" v-on="on">
                            <v-icon left>warning</v-icon>
                            無法儲存
                    </v-btn>  
                </template>
                <span>請確認好輸入規則</span>
            </v-tooltip>
        </div>

    </div>
</template>

<script>
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
import Control from "../components/Excel/Control.vue"
import ImportDialog from "../components/Excel/ImportDialog.vue"
export default {
    name: "excel_control",
    components: {
        Control,
        ImportDialog,
    },
    computed:{
        date:{ //紀錄選擇的迴路
            get () {
                    return this.$store.state.date;
                },
            set (value) {
                this.$store.commit('set_Select_Date', value)
            }
        },
        select_file:{ //紀錄選擇的迴路
            get () {
                    return this.$store.state.select_file;
                },
            set (value) {
                this.$store.commit('set_Select_File', value)
            }
        },
        select_sheet:{  //紀錄選擇的工作表
            get () {
                return this.$store.state.select_sheet;
            },
            set (value) {
                this.$store.commit('set_Select_Sheet', value)
            }
        },
        rwd_width () { // v-card寬度
                switch (this.$vuetify.breakpoint.name) {
                case 'xs': return "95%"
                case 'sm': return "90%"
                case 'md': return '80%'
                case 'lg': return '70%'
                case 'xl': return '60%'
            }
        },
        dialog_width () { // dialog寬度
                switch (this.$vuetify.breakpoint.name) {
                case 'xs': return "90%"
                case 'sm': return "80%"
                case 'md': return '60%'
                case 'lg': return '50%'
                case 'xl': return '40%'
            }
        },
    },

    data(){
        return{
            date_menu: false,
            
            xlsx_name: {}, //接受後端GET到的資料(關於所有EXCEL資訊)
            sheet_info: [], //紀錄所有SHEET
            project_info:[], //記錄當下SHEET的EXCEL資料

            /* Floating Btn */
            fab: false,
            floatBtn_dialog: false, // Floating按鈕的 Dialog
            import_dialog: false, // 匯入報表的 Dialog

            search: '', // 跳轉Dialog搜尋

            // 表格標頭
            table_header: [
                {text: '施工項目', value: 'name'},
                {text: '施工目標', value: 'total'},
                {text: '完成量', value: 'input'},
            ],
            show_submit_btn: true, // 因為 Tab的關係，只有第一個(工程進度)必須顯示，其他則不用

            allow_save: true,
            showToolTip: true,
        }
    },
    watch:{
        // 資料做變更時，重新將資料做統整(觸發條件: 日期變更)
        xlsx_name:{
            deep: true,
            handler(newVal, oldVal){
                // 如果舊值為空的話，則不執行(避免起始畫面時會有Error，因為一開始還未載入 xlsx_name)
                if( Object.keys(oldVal).length > 0 ){
                    this.change_Sheet()
                }
            }
        }
    },

    async created(){  // 網頁載入時，一開始就載入
        await this.excel_info() 
        this.select_file = ""
        this.select_sheet = ""
    },

    methods:{
        allow_save_method(val){
            console.log(val);
            this.allow_save = val
        },

        excel_info(query="") { //取得excel相關資訊(權重、項目名稱等..)
            query = query ? `?select_date=${query}`: "";
            axios.get(`/api/excel_write/${query}`).then(
                response => {
                    const map = {}
                    for (const item of response.data) {
                        const excel_name = Object.keys(item)[0]; // 得到Excel檔案名稱
                        map[excel_name] = {};
                        for(const sheet of Object.values(item)[0]){
                            const sheet_name = Object.keys(sheet)[0]; // 得到工作表名稱
                            const sheet_data = Object.values(sheet)[0]; // 得到該工作表工作表的資料(施工項目、最後一次更新時間)
                            map[excel_name][sheet_name] = sheet_data 
                        }
                    }
                    this.xlsx_name = Object.assign({}, map); // 將資料渲染到 data中
                    this.$store.commit("set_Xlsx_Name", this.xlsx_name)
                }).catch( error =>{
                    // console.log(error);
                    // 發現問題，則打開提示alert(檔案開著的問題)
                    this.$swal.fire({
                            icon: 'error',
                            title: error.response.data.title,
                            text: error.response.data.message,
                            footer: `<span>${error.response.data.footer}</span>`,
                            confirmButtonText: "確認關閉",
                        }
                    ).then((result) => {
                        /* Read more about isConfirmed, isDenied below */
                        // 點擊 ok，重新讀取資料，如果檔案還是開著，則會繼續報錯
                        if (result.isConfirmed) {
                            this.excel_info()
                        }
                    })
                })
                
        },

        post_excel() {  //將使用者填表單資料送到後端
        /* 表單 POST資料格式準備 */
            let formData = new FormData;
            formData.append('select_date',this.date) //紀錄日期
            formData.append('select_loop',this.select_file) //紀錄迴路
            formData.append('select_plant',this.select_sheet) //紀錄工作表
            for (const info of this.project_info){ //{ 項目名稱：[完成量,完成率] }
                formData.append(info.name, [Number(info.input), Number(info.input)/Number(info.total)*100])
            }

            axios({  //發送POST請求給後端
                method: 'post',
                url: '/api/excel_write/',
                xstfCookieName: 'csrftoken',
                xsrfHeaderName: 'X-CSRFToken',
                data: formData,
                responseType: 'json',
                headers: {
                    'X-CSRFToken': 'csrftoken',
                }
            }).then(response => {
                const statusCode = response.status // HTTP狀態碼
                // 輸入成功(201=代表輸入成功)
                if(statusCode === 201){
                    this.excel_info(this.date) // 輸入成功後，重新載入資料
                    this.$swal.fire({
                            icon: 'success',
                            title: response.data.message,
                        }
                    )
                // 請求確認成功，但需要再提醒資料備份問題 (202)
                }else if(statusCode === 202){
                    this.$swal.fire({
                        icon: 'info',
                        title: '備份通知',
                        text: '上次紀錄時間已超過一週以上，建議備份資料',
                        showDenyButton: true,
                        showCancelButton: true,
                        denyButtonText: `不須備份`,
                        cancelButtonText: `稍後再說`,
                        confirmButtonText: `立即備份`,
                    }).then(result=>{
                        // 直接按確定: 代表要儲存，讓使用者選擇要存入到哪一個資料夾
                        if(result.isConfirmed){
                            this.$swal.fire({
                                    icon: 'info',
                                    title: response.data.message,
                                    input: 'text',
                                    inputLabel: '填入資料夾名稱',
                                    showCloseButton: true,
                                    showCancelButton: true,
                                    cancelButtonText: "取消",
                                    confirmButtonText: "確定",
                                    allowOutsideClick: false, // 不能點擊外面關閉
                                    inputValue: "",
                                    inputValidator: (value) => {
                                        if (!value) {
                                            return '您必須填入資料夾名稱才能做檔案備份' // 沒填入資料時將會顯示
                                        }
                                    }
                            }).then(result=>{
                                if(result.isConfirmed){ // 確定要儲存
                                    const input_val = result.value // 剛剛輸入框的值
                                    axios.get(`/api/saveReport/${input_val}/${this.select_file}`) // 呼叫儲存API
                                        .then( res=>{
                                            axios.get(`/api/clear/${this.select_file}/${this.select_sheet}`).then(res=>{ // 儲存完後，還要記得清除重新刷新資料及更新內容
                                                this.post_excel();
                                            })
                                        }).catch( err=>{
                                            this.$swal.fire({
                                                icon: 'warning',
                                                title: '儲存失敗',
                                                text: msg,
                                            })
                                        })
                                }
                            })
                        }
                        // 拒絕: 直接輸入更新資料就好，不用再儲存備份資料夾
                        else if(result.isDenied){
                            this.$swal.fire({
                                icon: 'warning',
                                title: '注意',
                                text: '這個操作將會讓您遺失先前紀錄，請問還是要繼續嗎?',
                                showCancelButton: true,
                                cancelButtonText: '取消',
                                confirmButtonText: '確定',
                            }).then((result)=>{
                                // 如果按確定
                                if(result.isConfirmed){
                                    axios.get(`/api/clear/${this.select_file}/${this.select_sheet}`).then(res=>{
                                        this.post_excel();
                                    })
                                }
                            })
                        }
                    })
                }

            }).catch(error =>{
                const statusCode = error.response.status
                if(statusCode === 400){
                    this.$swal.fire({
                            icon: 'error',
                            title: `<label>${error.response.data.message}</label>`,
                        }
                    )
                }
            });

        },

        change_File(){ // 當選擇迴路時觸發
            this.project_info.length = 0; // 清空上一筆資料
            this.select_sheet = ""; // 重新選擇廠區
            this.sheet_info = Object.keys(this.xlsx_name[this.select_file]); // 直接從Excel總資料那邊抓取當前選擇Excel檔案的內容(工作表列表)
        },

        change_Sheet(){ // 當選擇廠區時觸發
            const response = JSON.parse(JSON.stringify(this.xlsx_name[this.select_file][this.select_sheet]));
            this.project_info.length = 0; // 清空上一筆資料
            // 弄成新的陣列
            for (const [key, value] of Object.entries(response.data)) {
                this.project_info.push({
                    name: key, // 施工項目
                    weight: value[0], // 權重
                    total: value[1], // 施工目標(總量)
                    input: value[2] !== "" ? value[2] : 0, // 完工量
                })
            }
        },

        // 變更日期來呈現不同日期的資料(只限一週內)
        changeDatePicker(date){
            this.excel_info(date)
        },

        // 清除所有輸入
        clear_project(){
           for(const info of this.project_info){
               info.input = 0
           }
        },

        // 完成率數值處理 (取百分比到小數點第二位)
        complete_Percentage(val){
            return isNaN(val) ? "0%" : `${Math.round(val * 10000) / 100.00 }%`
        },

        // 操作表格列
        handleTableRowClick(event){
            this.goAnchor(event.name); // 觸發錨點
            this.floatBtn_dialog = false; // 關閉 dialog
        },
        // 【錨點操作】
        // https://stackoverflow.com/questions/37270787/uncaught-syntaxerror-failed-to-execute-queryselector-on-document
        goAnchor(selector) {
            document.getElementById(selector).scrollIntoView({behavior: "smooth"});
        },
    },
}
</script>

