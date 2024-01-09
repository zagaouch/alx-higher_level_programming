#!/usr/bin/node

const file = require('./100-data.js');
const list = file.list;
const newlist = list.map((item, index) => item * index);
console.log(list);
console.log(newlist);
