#!/usr/bin/node

// Script prints two arguments passed to it, in the following format: “ is ”.
const firstArg = process.argv[2] || 'undefined';
const secondArg = process.argv[3] || 'undefined';

console.log(`${firstArg} is ${secondArg}`);
