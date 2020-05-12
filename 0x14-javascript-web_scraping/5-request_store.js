#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const fs = require('fs');

request.get(args[0], (error, reponse) => {
  if (error) {
    console.log(error);
  } else {
    const data = reponse.body;
    fs.writeFile(args[1], data, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
