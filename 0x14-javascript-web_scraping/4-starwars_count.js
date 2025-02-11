#!/usr/bin/node

const request = require('request');

// Get the API URL from command-line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  if (!data.results) {
    console.error('Invalid API response');
    return;
  }

  let count = 0;

  // Iterate through all movies and check if Wedge Antilles is in the characters list
  data.results.forEach((film) => {
    if (film.characters.some((charUrl) => charUrl.includes('/18/'))) {
      count++;
    }
  });

  console.log(count);
});
