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
    request(filmUrl, (error, response,body) => {
        if (error || response.statusCode !== 200) {
            console.error("Failed to fetch from starwar api");
            return;
        }
        getResponse = JSON.parse(body);
        getAllCharacters = getResponse.characters;
        const resolveCharacters = getAllCharacters.map(characters => {
            return new Promise((resolve, reject) => {
                request(characters, (error, response, body) => {
                    if (error || response.statusCode !== 200) {
                        console.error("Failed to fetch from characters");
                        return;
                    }
                    const getCharacterjson = JSON.parse(body);
                    resolve (getCharacterjson.name);
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