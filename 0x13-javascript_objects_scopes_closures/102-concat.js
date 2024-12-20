#!/usr/bin/node

// Script for concatenating 2 files.

// import the fs module
const fs = require('fs');
// retrieve command line arguments
const args = process.argv.slice(2); // ignore 1st two args

// Check if all 3 files paths provided.
if (args.length < 3) {
  console.error('usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}
// Extract file paths
const [file1, file2, destination] = args;

try {
  const content1 = fs.readFileSync(file1, 'utf-8');
  const content2 = fs.readFileSync(file2, 'utf-8');

  // Concatenate the content
  const combinedContent = `${content1}\n${content2}`;

  fs.writeFileSync(destination, combinedContent, 'utf-8');
} catch (error) {
  // Handle errors gracefully
  console.error('Error:', error.message);
  process.exit(1);
}
