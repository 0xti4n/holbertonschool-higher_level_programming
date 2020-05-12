#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${args[0]}`;
request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 404) {
    console.log(response.statusCode);
  } else {
    const data = JSON.parse(response.body);
    console.log(data.title);
  }
});
