const fs = require('fs');
module.exports = {
    devServer: {
        // disableHostCheck: true,
        https: true,
        host: "localhost",
        https: {
　　　key : fs.readFileSync('../server.key'),
　　　cert: fs.readFileSync('../server.crt'),
　　// ca : fs.readFileSync(”),
　　}
　},
}