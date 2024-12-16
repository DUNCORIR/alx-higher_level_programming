#!/usr/bin/node

// Script that  prints the addition of 2 integers.

function add (a, b) {
  return a + b;
}

const num1 = parseInt(process.argv[2]); // Convert the first argument to an integer.
const num2 = parseInt(process.argv[3]); // Convert the second argument to an integer

console.log(add(num1, num2));
