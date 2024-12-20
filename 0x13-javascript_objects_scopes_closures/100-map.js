#!/usr/bin/node

// Script that imports an array and computes a new array.
const list = require('./100-data').list;
// Create a new array using map
const newList = list.map((value, index) => value * index);

// prints originals and new arrays
console.log(list);
console.log(newList);
