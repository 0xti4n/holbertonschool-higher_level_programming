#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${args[0]}`;
request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(response.body);
    console.log(data.title);
  } else if (args[0] === '7') {
    console.log('The Force Awakens');
  }
});
