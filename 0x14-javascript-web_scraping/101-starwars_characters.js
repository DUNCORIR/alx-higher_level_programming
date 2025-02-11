#!/usr/bin/node

const request = require('request');

// Get movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./8-starwars_characters.js <Movie_ID>');
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

    if (!movieData.characters || movieData.characters.length === 0) {
      console.error('No characters found.');
      return;
    }

    // Fetch characters in order using promises
    const fetchCharacter = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            try {
              const characterData = JSON.parse(charBody);
              resolve(characterData.name);
            } catch (parseError) {
              reject(parseError);
            }
          }
        });
      });
    };

    // Process all character requests sequentially
    const fetchCharactersInOrder = async () => {
      for (const characterUrl of movieData.characters) {
        try {
          const name = await fetchCharacter(characterUrl);
          console.log(name);
        } catch (err) {
          console.error(err);
        }
      }
    };

    fetchCharactersInOrder();
  } catch (parseError) {
    console.error('Error parsing movie data:', parseError);
  }
});
