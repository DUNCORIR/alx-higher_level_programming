#!/usr/bin/node

// Script that prints a square.
const size = parseInt(process.argv[2]); // convert the first argument.

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
