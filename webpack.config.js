const path = require("path");

module.exports = {
  mode: "development",
  devtool: false,
  entry: {
    app: "./seism-jp/static/js/index.js",
  },
  output: {
    path: path.resolve(__dirname, "seism-jp/static/js/bundles"),
    filename: "[name].js",
  },
}
