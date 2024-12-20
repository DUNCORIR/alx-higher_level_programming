#!/usr/bin/node

//  Function that prints the number of arguments already printed and the new argument value.
let counter = 0;

exports.logMe = function (item) {
  // Print the current count and the item
  console.log(`${counter}: ${item}`);
  // Increment the counter for the next call
  counter++;
};
