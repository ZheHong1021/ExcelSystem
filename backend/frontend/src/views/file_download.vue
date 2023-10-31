<template>
    <div>
        <v-dialog
            transition="dialog-bottom-transition"
            max-width="600"
            v-model="dialog"
        >
            <template v-slot:default="dialog">
            <v-card>
                <v-toolbar color="primary" dark>功能介紹</v-toolbar>

                <v-card-text class="my-4">
                    <!-- 電腦版 -->
                    <v-stepper v-if="step_show_big"  v-model="e6">
                        <v-stepper-header>
                            <!-- Step 01 -->
                            <v-stepper-step :complete="e6 >1" step="1" @click="e6 = 1">
                                選擇資料夾
                            </v-stepper-step>
                            <v-divider></v-divider>

                            <!-- Step 02 -->
                            <v-stepper-step :complete="e6 > 2" step="2" @click="e6 = 2">
                                點擊檔案下載
                            </v-stepper-step>
                            <v-divider></v-divider>

                            <!-- Step 03 -->
                            <v-stepper-step :complete="e6 > 3" step="3" @click="e6 = 3">
                                下載完成
                            </v-stepper-step>
                            <v-divider></v-divider>
                        </v-stepper-header>

                        <v-stepper-items>
                            <!-- Step 01 -->
                            <v-stepper-content step="1">
                                <v-card color="grey lighten-1" class="mb-12" height="200px">
                                    <v-img src="../assets/images/steps/download/PC/step01.png"></v-img>
                                </v-card>
                            </v-stepper-content>

                            <!-- Step 02 -->
                            <v-stepper-content step="2">
                                <v-card color="grey lighten-1" class="mb-12" height="200px">
                                    <v-img src="../assets/images/steps/download/PC/step02.png"></v-img>
                                </v-card>
                            </v-stepper-content>

                            <!-- Step 03 -->
                            <v-stepper-content step="3">
                                <v-card color="grey lighten-1" class="mb-12" height="200px">
                                    <v-img src="../assets/images/steps/download/PC/step03.png"></v-img>
                                </v-card>
                            </v-stepper-content>

                        </v-stepper-items>
                    </v-stepper>

                    <!-- 手機板 -->
                    <v-stepper v-else v-model="e6" vertical>
                        <!-- Step 01 -->
                        <v-stepper-step :complete="e6 > 1" step="1" @click="e6 = 1">
                            選擇資料夾
                        </v-stepper-step>
                        <v-stepper-content step="1">
                            <v-card color="grey lighten-1" class="mb-12" height="200px">
                                <v-img src="../assets/images/steps/download/mobile/step01.png"></v-img>
                            </v-card>
                        </v-stepper-content>

                        <!-- Step 02 -->
                        <v-stepper-step :complete="e6 >2" step="2" @click="e6 = 2">
                            點擊檔案下載
                        </v-stepper-step>
                        <v-stepper-content step="2">
                            <v-card color="grey lighten-1" class="mb-12" height="200px">
                                 <v-img src="../assets/images/steps/download/mobile/step02.png"></v-img>
                            </v-card>
                        </v-stepper-content>

                        <!-- Step 03 -->
                        <v-stepper-step :complete="e6 > 3" step="3" @click="e6 = 3">
                            下載完成
                        </v-stepper-step>
                        <v-stepper-content step="3">
                            <v-card color="grey lighten-1" class="mb-12" height="200px">
                                 <v-img src="../assets/images/steps/download/mobile/step03.png"></v-img>
                            </v-card>
                        </v-stepper-content>
                    </v-stepper>
                </v-card-text>

                <v-card-actions class="justify-end">
                    <v-btn text @click="dialog.value = false" color="primary" class="font-weight-bold">關閉</v-btn>
                </v-card-actions>
            </v-card>
            </template>
        </v-dialog>

        <v-card :width="rwd_width" class="mx-auto my-8 pa-4">
            <v-row>
                <v-col cols="12" class="my-0 d-flex align-center">
                    <!-- Tooltip -->
                    <v-tooltip bottom>
                        <template v-slot:activator="{ on, attrs }">
                            <v-chip v-bind="attrs" v-on="on"
                                @click="dialog = true"
                                color="light-blue darken-4" class="white--text mb-4 font-weight-bold" label style="cursor: pointer;">
                                <v-icon left color="white">file_download</v-icon>
                                報表下載
                            </v-chip>
                        </template>
                        <!-- Tooltip Content -->
                        <span>點擊打開功能介紹</span>
                    </v-tooltip>
                    <v-btn color="blue darken-1" class="white--text ml-auto" @click="download_Zipfile">
                        <v-icon left>download_for_offline</v-icon>
                        一鍵下載
                    </v-btn>
                </v-col>
                <v-col cols="12" class="my-0">
                    <v-expansion-panels focusable inset >
                        <v-expansion-panel v-for="(files, folder) in folder_list" :key="folder">
                            <v-expansion-panel-header>
                                <!-- 因為 icon跟文字之間並沒有垂直置中 -->
                                <label class="d-flex align-center">
                                    <v-icon color="orange darken-1" class="mr-2">folder</v-icon>
                                    {{folder}}

                                    <!-- 只有在 PC介面會顯示 -->
                                    <span class="ml-auto mr-4 text-subtitle-2 grey--text" v-if="step_show_big">創建日期: {{ files.create_date }}</span>
                                </label>
                                
                                <template v-slot:actions>
                                    <!-- 讀取該資料夾內的檔案數量 -->
                                    <v-avatar 
                                        :color="files.data.length > 0 ? 'green darken-3' : 'grey'" 
                                        class="white--text" size="24" >
                                        {{ files.data.length > 0 ? files.data.length : 0 }}
                                    </v-avatar>
                                    <v-icon color="primary">$expand</v-icon>
                                </template>
                            </v-expansion-panel-header>

                            <v-expansion-panel-content>
                                <template v-if="files.data.length !== 0">
                                    <!-- 只有在 Mobile介面會顯示 -->
                                    <span class="text-caption grey--text"  v-if="!step_show_big">創建日期 {{ files.create_date }}</span>

                                    <!-- 抓取資料夾內所有的Excel檔案(透過Django所設定的 api來抓取excel) -->
                                    <div v-for="(file, index) in files.data" :key="index" class="my-4 d-flex align-center">
                                        <span class="download_link">
                                            <a :href="`/api/excel_download?folder=${folder}&filename=${file}`" download>
                                                <v-icon color="green darken-2" class="mr-1">description</v-icon>
                                                <label>{{file}}</label>
                                            </a>
                                        </span>
                                    </div>


                                </template>
                                <template v-else>
                                    <div class="mt-4">
                                        目前該資料夾並無檔案
                                    </div>
                                </template>

                            </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-expansion-panels>

                </v-col>
            </v-row>

        </v-card>
    </div>

</template>

<script>
import axios from 'axios';
import {Zip_Folder, Download_Zip, remove_Zip} from "@/api"
export default {
    name: "file_download",
    data(){
        return{
            // 所有已被儲存的資料夾
            folder_list: {},
            dialog: false,
            e6: 1,
        }
    },
    computed:{
      rwd_width () {
        switch (this.$vuetify.breakpoint.name) {
          case 'xs': return "100%"
          case 'sm': return "90%"
          case 'md': return '80%'
          case 'lg': return '70%'
          case 'xl': return '60%'
        }
      },

      step_show_big(){
          switch (this.$vuetify.breakpoint.name) {
            case 'xs': return false;
            case 'sm': return false;
            case 'md': return true;
            case 'lg': return true;
            case 'xl': return true;
        }
      }
    },
    created(){  // 網頁載入時，一開始就載入
        axios.get('/api/folderList/').then(
            res => {
                this.folder_list = res.data
            },
            error => {
                alert(error) //沒接收到 印出ERROR
            }
        )
    },
    methods:{
        download_Zipfile(){
            Zip_Folder()
                .then(res=>{
                    if(res.status === 200){
                        this.downloadAPI()
                    }
                })
                .catch(err=>{
                    console.log(err);
                })
        },


        async downloadAPI(){
            await Download_Zip()
                .then(res=>{
                    if(res.status === 200){
                        window.open("/api/download_zip/") // 打開下載
                        setTimeout(() => { // 20秒後自動將壓縮檔刪掉
                            remove_Zip()
                        }, 20 * 1000);
                    }
                })
                .catch(err=>{
                    if(err.response.status === 404){
                        this.$swal.fire("找不到檔案", "抱歉，發生了一些錯誤", "warning")
                    }
                })
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
    .download_link{
        cursor: pointer;

        &:hover label{
            color: #fa0;
            border-bottom: 2px solid #fa0;
        }
    }
</style>
