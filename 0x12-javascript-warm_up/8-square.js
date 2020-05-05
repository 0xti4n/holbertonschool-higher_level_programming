#!/usr/bin/node

const process = require('process');

const args = process.argv;
const letter = 'X';

if (parseInt(args[2])) {
  for (let col = 0; col < parseInt(args[2]); col++) {
    console.log(letter.repeat(parseInt(args[2])));
  }
} else {
  console.log('Missing size');
}
