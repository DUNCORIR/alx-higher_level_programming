#!/usr/bin/node

// Script prints My number: <first argument converted in integer> if the first argument can be converted to an integer.
const firstArg = process.argv[2]; // Get first argument
const number = parseInt(firstArg); // Attempt conversion to int.

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
