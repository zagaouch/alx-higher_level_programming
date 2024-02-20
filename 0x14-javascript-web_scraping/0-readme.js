#!/usr/bin/node
// Read from file

const fs = require('fs');
const filePath = process.argv[2]; 
function readFileContent(filePath) {
    fs.readFile(filePath, 'utf-8', (err, data) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log(data);
    });
}