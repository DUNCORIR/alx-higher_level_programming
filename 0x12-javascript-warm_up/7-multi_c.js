#!/usr/bin/node

// Script  prints x times “C is fun”.

const x = parseInt(process.argv[2]); // Convert the first argument to an integer.

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
