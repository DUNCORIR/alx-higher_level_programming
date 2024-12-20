#!/usr/bin/node

// Script that returns the reversed version of a list.
exports.esrever = function (list) {
  // Initialize an empty array for reversed elements.
  const reversedList = [];

  // Loop through the array from end to start
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  // Reversed Array reversed.
  return reversedList;
};
