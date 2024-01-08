#!/usr/bin/node
const args = process.argv; // Array of arguments

if (args.length === 3 && parseInt(args[2])) { // If there is an argument and it can be converted to an integer
  console.log('My number:', parseInt(args[2]));
} else { // If there is no argument or the argument is not an integer
  console.log('Not a number');
}
