#!/usr/bin/node
// wite from file

const filesys = require('fs');
filesys.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
    }
  });
