#!/usr/bin/node
function factorial (n) { // n is the number to be factorialized
  if (!n) { // if n is 0, return 1
    return 1;
  }
  return n * factorial(n - 1); // otherwise, return n * the factorial of n - 1
}

console.log(factorial(process.argv[2])); // print the factorial of the number passed in as an argument
