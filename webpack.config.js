const path = require("path");

module.exports = {
  mode: "development",
  devtool: false,
  entry: {
    earthquakes: "./seism-jp/static/js/earthquakes/index.js",
    volcanoes: "./seism-jp/static/js/volcanoes/index.js",
  },
  output: {
    path: path.resolve(__dirname, "seism-jp/static/js/bundles"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.scss/,
        use: [
          "style-loader",
          {
            loader: "css-loader",
            options: {
              url: false
            }
          },
          {
            loader: "sass-loader",
          }
        ]
      }
    ]
  }
}
