<template>
    <header class="masthead" style="min-height: 100vh;">
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="accordion accordion-flush" id="accordionFlushExample">

                    <!-- 讀取多少有多少資料夾 -->
                    <div class="accordion-item" v-for="(files, folder) in folder_list" :key="folder">
                        <h2 class="accordion-header" :id="`flush-heading-${folder}`">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" :data-bs-target="`#flush-collapse-${folder}`" aria-expanded="false" :aria-controls="`flush-collapse-${folder}`">
                            <!-- 顯示資料夾名稱 -->
                            {{folder}}
                        </button>
                        </h2>
                        <template v-if="files.length !== 0">
                            <!-- 抓取資料夾內所有的Excel檔案(透過Django所設定的 api來抓取excel) -->
                            <div v-for="(file, index) in files" :key="index" :id="`flush-collapse-${folder}`" class="accordion-collapse collapse my-4" :aria-labelledby="`flush-heading-${folder}`" data-bs-parent="#accordionFlushExample">
                                <a :href="`/api/excel_download?folder=${folder}&filename=${file}`" download>{{file}}</a>
                            </div>
                        </template>
                         <template v-else>
                             <div :id="`flush-collapse-${folder}`" class="accordion-collapse collapse my-4" :aria-labelledby="`flush-heading-${folder}`" data-bs-parent="#accordionFlushExample">
                                 目前該資料夾並無檔案
                            </div>
                         </template>
                    </div>

                </div>
            </div>
        </div>
    </header>
</template>

<script>
import axios from 'axios';
export default {
    name: "file_download",
    data(){
        return{
            // 所有已被儲存的資料夾
            folder_list: {},

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

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    
</style>
