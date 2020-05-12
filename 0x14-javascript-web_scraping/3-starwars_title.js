#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + args[0];

request.get(url, (error, response) => {
  if (error) console.log(error);
  const data = JSON.parse(response.body);
  console.log(data.title);
});
