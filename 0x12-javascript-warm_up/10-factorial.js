#!/usr/bin/node

const process = require('process');

const args = process.argv;

function factorialize (num) {
  if (num === 0) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}

if (parseInt(args[2])) {
  console.log(factorialize(parseInt(args[2])));
} else {
  console.log(1);
}
