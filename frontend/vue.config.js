const fs = require('fs');
module.exports = {
    devServer: {
        // disableHostCheck: true,
        https: true,
        // host: '0.0.0.0',
        https: {
　　　key : fs.readFileSync('../server.key'),
　　　cert: fs.readFileSync('../server.crt'),
　　}
　},
}