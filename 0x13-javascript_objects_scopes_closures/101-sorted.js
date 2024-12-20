#!/usr/bin/node

// Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
// Import the dictionary
const dict = require('./101-data').dict;

// create a new dict
const newDict = {};

// populate new dict
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}

// print new dict
console.log(newDict);
