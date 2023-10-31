<template>
    <v-container 
        class="d-flex align-center justify-center pa-4"
        style="min-height: 80vh; width: 100%;">
            <v-row class="text-center" >
                <v-col cols="12">
                    <h3 class="text-h3 font-weight-bold white--text">歡迎使用 Excel系統!</h3>
                </v-col>

                <v-col cols="12" class="mt-12">
                    <h4 class="text-h4 font-weight-bold">
                        <v-btn rounded color="success" dark x-large @click="$router.push('/ExcelControl')">
                            <v-icon class="mr-2">start</v-icon>
                            Start
                        </v-btn>
                    </h4>
                </v-col>
            </v-row>
    </v-container>
</template>

<script>
export default {
    name: "home-page"
}
</script>

