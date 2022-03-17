<template>
  <main>
    <Nav/>
    <router-view></router-view>
    <Footer/>
  </main>
</template>

<script>
import Nav from './components/nav.vue';
import Footer from './components/footer.vue';
export default {
  name: 'App',
  components: {
    Nav,
    Footer,
  }
}
</script>

<style>

</style>