#!/usr/bin/node

const request = require("request");

// Extract movie ID from command line arguments
const movieId = process.argv[2];

// Check if movie ID is provided
if (!movieId) {
  console.error("Usage: ./script.js <Movie ID>");
  process.exit(1);
}

// Function to fetch and print character names for a given movie ID
const printCharacterNames = (movieId) => {
  const url = `https://swapi-api.alx-tools.com/api/${movieId}/`;

  // Fetch movie details
  request(url, (error, response, body) => {
    if (error) {
      console.error(`Error fetching movie data: ${error.message}`);
      process.exit(1);
    }

    if (response.statusCode !== 200) {
      console.error(
        `Failed to fetch movie data. Status code: ${response.statusCode}`
      );
      process.exit(1);
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Fetch and print character names
    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(`Error fetching character data: ${charError.message}`);
          process.exit(1);
        }

        if (charResponse.statusCode !== 200) {
          console.error(
            `Failed to fetch character data. Status code: ${charResponse.statusCode}`
          );
          process.exit(1);
        }

        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    });
  });
};

// Run the function with the provided movie ID
printCharacterNames(movieId);
