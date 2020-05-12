#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

request.get(args[0], (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const newDict = {};
    data.forEach(i => {
      if (i.userId) {
        if (i.completed === true) {
          if (newDict[i.userId]) {
            newDict[i.userId] += 1;
          } else {
            newDict[i.userId] = 1;
          }
        }
      }
    });
    console.log(newDict);
  }
});
