#!/usr/bin/node
const args = process.argv; // Array of arguments

if (args[2]) { // If exists the first argument
  console.log(args[2]);
} else { // If there are no arguments
  console.log('No argument');
}
