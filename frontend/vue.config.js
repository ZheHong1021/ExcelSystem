module.exports = {
    // 關閉語法檢查
    // lintOnSave: false,
    devServer: {
      disableHostCheck: true,
      proxy: {
        '/api': {
          target: 'http://localhost:8000/',
          pathRewrite: {
            '^/api': 'api/'
          },
          ws: true, // 用於支援 websocket
          changeOrigin: true // 用於控制請求投中的 Host 值
        }
      }
    }
  }