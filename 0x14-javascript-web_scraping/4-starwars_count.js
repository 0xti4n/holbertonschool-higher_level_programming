#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

request(args[0], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body).results;
      let con = 0;
      for (let i = 0; i < data.length; i++) {
        const dataCharacteres = data[i].characters;
        if (dataCharacteres.indexOf('https://swapi-api.hbtn.io/api/people/18/') !== -1) {
          con++;
        }
      }
      console.log(con);
    }
  }
});
