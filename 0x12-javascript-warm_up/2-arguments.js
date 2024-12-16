#!/usr/bin/node

// The script prints a message depending of the number of arguments passed.
const args = process.argv.length - 2; // No of args passed.

if (args === 0) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
