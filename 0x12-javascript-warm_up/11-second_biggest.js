#!/usr/bin/node

const process = require('process');

const args = process.argv;

let first = 0;
let second = 0;

if (!args[2]) {
  console.log(0);
} else {
  if (args.length === 3) {
    console.log(0);
  } else if (args.length > 3) {
    for (let i = 2; i < args.length; i++) {
      if (args[i] > first) {
        second = first;
        first = args[i];
      } else if (args[i] > second && args[i] !== first) {
        second = args[i];
      }
    }
    console.log(parseInt(second));
  }
}
