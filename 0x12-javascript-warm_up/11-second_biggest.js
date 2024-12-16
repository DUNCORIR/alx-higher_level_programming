#!/usr/bin/node

// Script that  searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2).map(Number); // Get arguments and convert to integers

if (args.length < 2) {
  console.log(0); // Print 0 if there are no or only 1 argument
} else {
  args.sort((a, b) => b - a); // Sort numbers in descending order
  console.log(args[1]); // Print the second largest number
}
