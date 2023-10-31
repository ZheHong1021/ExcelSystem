<template>
  <v-app class="img">
    <Nav/>
    <v-main class="view_container">
      <v-container fluid>
            <keep-alive>
              <router-view></router-view>
            </keep-alive>
      </v-container>
    </v-main>
    <Footer/>
  </v-app>


</template>


<script>
import Nav from './components/nav.vue';
import Footer from './components/footer.vue';
export default {
  name: 'App',
  components: {
    Nav,
    Footer,
  },
  data(){
    return {
      drawer: false,
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC&family=Roboto&display=swap');
  *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    transition: .25s;
    font-family: 'Noto Sans TC', sans-serif;
    font-family: 'Roboto', sans-serif;
  }
  html {
    scroll-behavior: smooth;
  }
  body{
    font-size: 100%;
  }

  a{
    list-style: none;
    text-decoration:none;
  }

  .view_container{
    margin-top: 120px; /* margin-top: 是為了讓 v-app-bar的 fixed可以正常使用*/
  }

  /* https://stackoverflow.com/questions/60814110/vuetify-set-background-img */
  #app{
    background: 
      linear-gradient(to bottom, rgba(92, 77, 66, 0.9) 0%, rgba(92, 77, 66, 0.9) 100%), 
      url("./assets/images/background.jpg");
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: scroll;
    background-size: cover;
  }

    /* 全體字型的RWD設定 */
    @media screen and (max-width: 1440px) {
        body{
          font-size: 95%;
        }
    }
    @media screen and (max-width: 1024px) {
        body{
          font-size: 90%;
        }
    }

    @media screen and (max-width: 768px) {
        body{
          font-size: 85%;
        }
    }
    @media screen and (max-width: 578px) {
        body{
          font-size: 80%;
        }
    }

  /* ScrollBar Style */
  ::-webkit-scrollbar-track
  {
    box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    border-radius: 10px;
    background-color: #F5F5F5;
  }

  ::-webkit-scrollbar
  {
    width: 8px;
    background-color: #F5F5F5;
  }

  ::-webkit-scrollbar-thumb
  {
    border-radius: 10px;
    box-shadow: inset 0 0 6px rgba(0,0,0,.3);
    background-color: #2d3436;
  }

</style>