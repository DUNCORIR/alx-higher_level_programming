#!/usr/bin/node

const request = require('request');

// Get the URL from command-line arguments
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
