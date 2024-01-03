#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;

    const printCharacter = (characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error(error);
        }
      });
    };

    charactersUrls.forEach(printCharacter);
  }
});

