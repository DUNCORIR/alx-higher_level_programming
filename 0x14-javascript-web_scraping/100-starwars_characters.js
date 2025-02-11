#!/usr/bin/node

const request = require('request');

// Get movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./7-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Construct API URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Fetch movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    // Parse JSON response
    const movieData = JSON.parse(body);

    if (!movieData.characters) {
      console.error('No characters found.');
      return;
    }

    // Fetch each character's name
    movieData.characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
          return;
        }
        try {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } catch (charParseError) {
          console.error('Error parsing character data:', charParseError);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing movie data:', parseError);
  }
});
