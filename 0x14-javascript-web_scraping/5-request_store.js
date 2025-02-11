#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

// Make a GET request to fetch the webpage content
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Write the response body to the specified file with UTF-8 encoding
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
