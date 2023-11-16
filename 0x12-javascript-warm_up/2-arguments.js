#!/usr/bin/node
const args = process.argv; // Array of arguments

if (args.length <= 2) { // If there are no arguments
  console.log('No argument');
} else if (args.length === 3) { // If there is one argument
  console.log('Argument found');
} else { // If there are more than one argument
  console.log('Arguments found');
}
