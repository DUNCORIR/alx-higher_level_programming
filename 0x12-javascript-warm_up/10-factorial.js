#!/usr/bin/node

// Script computes and prints a factorial where
// The first argument is integer (argument can be cast as integer)
// used for computing the factorial

function factorial (n) {
  if (n <= 1) {
    return 1; // Base case: 0! = 1 and 1! = 1
  }
  return n * factorial(n - 1); // Recursive case
}

const num = parseInt(process.argv[2]); // Convert the argument to an integer
console.log(factorial(isNaN(num) ? 1 : num)); // If NaN, treat as 1
