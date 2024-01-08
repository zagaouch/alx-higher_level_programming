#!/usr/bin/node
const str = 'X';
const i = process.argv[2]; // Get the second argument

if (i && parseInt(i)) { // If exists the first argument and it can be converted to an integer
  for (let j = 0; j < i; j++) { // Loop through the number of times
    console.log(str.repeat(i)); // Print the string repeated the number of times
  }
} else {
  console.log('Missing size'); // If there is no argument or the argument is not an integer
}
