#!/usr/bin/node

// Function that converts a number from base 10 to another base passed as argument.

exports.converter = function (base) {
  return function (num) {
    // Convert the number to the specified base
    return num.toString(base);
  };
};
