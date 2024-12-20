#!/usr/bin/node

// Script that returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  let count = 0; // Initialize counter
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++; // Increment counter if match found
    }
  }
  return count; // Return the total count
};
