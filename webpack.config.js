module.exports = {
    mode: process.env.NODE_ENV || "development",
    entry: ["./src/app.js"],
    output: {
        filename: "bundle.js",
        path: __dirname + "/dist"
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                use: "babel-loader",
                exclude: /node_modules/
            }
        ]
    }
};
