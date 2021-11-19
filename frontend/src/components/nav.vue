<template>
    <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
        <div class="container px-4 px-lg-5">
            <router-link class="navbar-brand" to="/">Excel系統</router-link>
            <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ms-auto my-2 my-lg-0">
                    <li class="nav-item"><router-link class="nav-link" to="/ExcelControl">填寫工作日報</router-link></li>
                    <li class="nav-item"><a class="nav-link" href="#services">Services</a></li>
                    <li class="nav-item"><a class="nav-link" href="#portfolio">Portfolio</a></li>
                    <li class="nav-item"><router-link class="nav-link" to="/FileDownload">檔案下載區</router-link></li>
                </ul>
            </div>
        </div>
    </nav>
</template>
<script>
export default {

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="../../public/css/styles.css">

</style>
