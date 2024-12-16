#!/usr/bin/node

// The add function that returns the sum of two integers
function add (a, b) {
  return a + b;
}

// Export the function so it can be used outside
module.exports.add = add;
