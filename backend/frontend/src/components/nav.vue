<template>
    <div>
        <v-navigation-drawer app 
            v-model="drawer"
            temporary>
            <v-list-item>
                <v-list-item-avatar>
                    <v-img src="https://s.yimg.com/uu/api/res/1.2/beAavHDSzDbuL9hOFBDodg--~B/aD02NzU7dz0xMjAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/zh-tw/ebc.net.tw/5e04714f157d2756325a0cb2eb67bf23"></v-img>
                </v-list-item-avatar>
                <v-list-item-content m-content>
                    <v-list-item-title>吉娃娃</v-list-item-title>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <!-- 功能列表 -->
            <v-list dense>
                <v-subheader>功能列表</v-subheader>
                <router-link :to="item.link" 
                    v-for="item in routes"
                    :key="item.title"
                    link>
                    <v-list-item :class="$route.path === item.link ? 'primary lighten-1 white--text' : ''">
                        <v-list-item-icon>
                            <v-icon :color="$route.path === item.link ? 'white' : '' ">{{ item.icon }}</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content>
                            <v-list-item-title>{{ item.title }}</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </router-link>
            </v-list>

            <v-divider></v-divider>

            <!-- 使用者操作 -->
            <v-list dense>
                <v-subheader>使用者操作</v-subheader>

                <router-link v-if="!is_login" to="/login">
                    <v-list-item :class="$route.path === '/login' ? 'primary lighten-1 white--text' : ''">
                        <v-list-item-icon>
                            <v-icon :color="$route.path === '/login' ? 'white' : '' ">login</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-title>登入</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </router-link>

                <a v-else @click.prevent="logout">
                    <v-list-item >
                        <v-list-item-icon>
                            <v-icon>logout</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-title>登出</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </a>
            </v-list>
        </v-navigation-drawer>

        <!-- 固定問題: https://stackoverflow.com/questions/57497145/how-to-set-v-sheet-v-container-size-to-match-screen-with-v-app-bar-in-vuetify-2 -->
        <v-app-bar color="#fcb69f" dark shrink-on-scroll prominent 
            src="../assets/images/background.jpg"
            fixed
            scroll-threshold="500"
            >
            <template v-slot:img="{ props }">
                <v-img
                    v-bind="props"
                    gradient="to bottom, rgba(92, 77, 66, 0.9) 0%, rgba(92, 77, 66, 0.9) 100%"
                ></v-img>
            </template>
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title class="text-h5 font-weight-bold">
            <router-link to="/" class="white--text" >
            Excel系統
            </router-link>
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <nav class="d-flex" v-if="!is_open_navbar">
            <router-link 
                :to="{path: route.link}" 
                v-for="route in routes" :key="route.link" 
                active-class="active" exact
                class="route-link">
                <v-toolbar-title class="mx-6 row-pointer text-Heading-6 font-weight-bold darken-1">{{route.title}}</v-toolbar-title>
            </router-link>
        </nav>

        <v-btn icon>
            <v-icon >mdi-dots-vertical</v-icon>
        </v-btn>
        </v-app-bar>
    </div>


</template>
<script>
import { mapState } from 'vuex';
export default {
    name: "Nav",
    computed:{
        ...mapState(['is_login']),
      // 只有在裝置寬度小於 960時，才會開啟
        is_open_navbar() {
          const rwd = this.$vuetify.breakpoint.name;
            if(rwd === 'xs' || rwd === 'sm'){
              return true;
            }
            return false;
        },
    },
    data(){
        return {
            drawer: false,
            // 功能列表
            routes: [
                { title: '首頁', icon: 'home', link: '/' },
                { title: '填寫工作日報', icon: 'save_as', link: '/ExcelControl' },
                { title: '檔案下載區', icon: 'get_app', link: '/FileDownload' },
                // { title: '測試', icon: 'cruelty_free', link: '/test' },
            ],

        }
    },

    methods:{
        logout(){
            this.$swal.fire({
                icon: 'info',
                title: '登出',
                text: '您確定要登出了嗎?',
                showCancelButton: true,
                cancelButtonText: '取消',
                confirmButtonText: '確定',
            }).then(result=>{
                if(result.isConfirmed){
                    this.$swal.fire('登出成功', '', 'success')
                    this.$store.commit("setLogin", false);
                    this.$router.push('/login')
                }
            })
        }
    }
}
</script>


<style lang="scss" scoped>
    // 沒有 active
    .route-link{
        color: #9E9E9E;
    }
    // 有 active
    .active{
        color: #f4623a;
    }
</style>
