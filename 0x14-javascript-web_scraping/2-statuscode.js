#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

request.get(args[0], (error, response) => {
  if (error) console.log(error);
  console.log(`code: ${response.statusCode}`);
});
