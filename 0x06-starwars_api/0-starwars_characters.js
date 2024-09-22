#!/usr/bin/node
/**
 * Extracting characters from the Star Wars API
 */
const request = require('request');
if (process.argv.length !== 3) {
    return;
}
const film_id = parseInt(process.argv[2], 10);
if (isNaN(film_id)) {
    return;
}

const filmUrl = `https://swapi.dev/api/films/${film_id}`;

function getCharacters() {
    request(filmUrl, (error, response, body) => {
        if (error || response.statusCode !== 200) {
            console.error("Failed to fetch data from star war endpoint");
            return;
        }
        const getResponse = JSON.parse(body);
        const getAllCharacters = getResponse.characters;
        const resolveCharacters = getAllCharacters.map(character => {
            return new Promise((resolve, reject) => {
                request(character, (error, response, body) => {
                    if (error || response.statusCode !== 200) {
                        console.error("Failed to fectch from character");
                        return;
                    }
                    const getCharacterjson = JSON.parse(body);
                    resolve(getCharacterjson.name);
                });
            });
        });
        Promise.all(resolveCharacters)
            .then(characters => characters.forEach(name => {
                console.log(name);
            })).catch(error => {
                console.error(error);
            });
    }); 
}

getCharacters();