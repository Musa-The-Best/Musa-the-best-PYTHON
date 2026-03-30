var fs = require('fs');
fs.appendFile('mynewtextfile.txt', 'This is my message in NodeJS', function (err) {
    if (err) throw err;
    console.log('Savred!');
}); ``