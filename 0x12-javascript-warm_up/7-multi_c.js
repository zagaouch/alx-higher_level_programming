#!/usr/bin/node
const str = 'C is fun';
const i = process.argv[2]; // Get the second argument

if (!parseInt(i)) {
  console.log('Missing number of occurrences');
}
for (let j = 0; j < i; j++) { // Loop through the number of times
  console.log(str); // Print the string
}
