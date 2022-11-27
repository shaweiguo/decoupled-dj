const path = require('path');
const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  publicPath: process.env.VUE_APP_STATIC_URL,
  outputDir: path.resolve(__dirname, "../../static", "billing"),
  indexPath: path.resolve(__dirname, "../../templates/", "billing", "index.html"),
  transpileDependencies: true,
  lintOnSave: false,
});
