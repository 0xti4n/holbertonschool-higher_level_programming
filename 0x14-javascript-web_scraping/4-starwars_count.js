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
        for (let j = 0; j < dataCharacteres.length; j++) {
          const splt = dataCharacteres[j].split('/');
          const res = splt.filter(element => element === '18');
          if (res.length > 0) {
            con++;
          }
        }
      }
      console.log(con);
    }
  }
});
