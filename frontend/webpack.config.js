"use strict";

var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  context: __dirname,
  entry: "./js/main",
  output: {
    path: path.resolve("./bundles/"),
    filename: "[name]-[hash].js",
    libraryTarget: "window",
  },

  // plugins: [new BundleTracker({ filename: "./webpack-stats.json" })],
  plugins: [
    new webpack.NoEmitOnErrorsPlugin(),
    new webpack.NamedModulesPlugin(),
    new BundleTracker({ filename: "./webpack-stats.json" }),
  ],

  module: {
    rules: [
      // we pass the output from babel loader to react-hot loader
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env", "@babel/preset-react"],
            plugins: ["@babel/plugin-proposal-class-properties", "@babel/plugin-transform-runtime"],
          },
        },
        // loaders: ["babel-loader"],
        // options: {
        //   presets: ["es2015", "react"],
        // },
      },
    ],
  },

  resolve: {
    modules: ["node_modules", "bower_components"],
    extensions: [".js", ".jsx"],
  },
};
