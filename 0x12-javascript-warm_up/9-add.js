#!/usr/bin/node

function add (a, b) {
    return Number(a) + Number(b); // Convert to number
  }
  
  console.log(add(process.argv[2], process.argv[3])); // Add the first and second argument
