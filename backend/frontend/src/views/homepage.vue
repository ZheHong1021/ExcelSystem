<template>
    <header class="masthead">
        <div class="container px-4 px-lg-5 h-100">
            <div class="row gx-4 gx-lg-5 h-100 align-items-center justify-content-center text-center">
                <div class="col-lg-8 align-self-end">
                    <h1 class="text-white font-weight-bold">Your Favorite Place for Free Bootstrap Themes</h1>
                    <hr class="divider" />
                </div>
                <div class="col-lg-8 align-self-baseline">
                    <p class="text-white-75 mb-5">Start Bootstrap can help you build better websites using the Bootstrap framework! Just download a theme and start customizing, no strings attached!</p>
                    <router-link class="btn btn-primary btn-xl" to="/ExcelControl">Start</router-link>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    name: "Home"
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    header {
        height: 100vh;
    }
</style>
