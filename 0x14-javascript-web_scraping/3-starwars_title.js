#!/usr/bin/node

const request = require('request');

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

// Construct the API URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  if (data.title) {
    console.log(data.title);
  } else {
    console.error('Movie not found');
  }
});
