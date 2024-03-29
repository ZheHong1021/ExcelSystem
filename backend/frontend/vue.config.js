const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  lintOnSave: false,
  transpileDependencies: [
    'vuetify'
  ],
  outputDir: 'dist',
  assetsDir: 'static', // 指定build時，在靜態文件上一層添加static目錄

  
  devServer: {
    historyApiFallback: true, // 路由設定History Mode(開發模式下而已，生產模式還要再去後端設定)

    open: true,
    host: 'localhost',  // 設置主機地址
    port: 8080,         // 設置默認埠號
    https: false,
    //以上的ip和埠號是我們本機的;下面為需要跨域的
    proxy: {    //配置跨域
      '/api': {
        // target: 'http://localhost:8000/',   //這裡後台的地址模擬的，應該填寫真實的後台api
        target: 'http://localhost/',   //這裡後台的地址模擬的，應該填寫真實的後台api
        // target: 'http://shrimp-test.com/',   //這裡後台的地址模擬的，應該填寫真實的後台api
        // target: 'https://shrimp-research.herokuapp.com/',   //這裡後台的地址模擬的，應該填寫真實的後台api
        ws: true,     // 如果要代理 websockets
        changOrigin: true,  //允許跨域
        // pathRewrite: {
          //  '^/api': '' //請求的時候使用這個api就可以
          // }
        }
        
      }
    },
    
    

})
