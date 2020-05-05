#!/usr/bin/node

const process = require('process');
const args = process.argv;
args.splice(0, 2);

if (!args[2]) {
  console.log(0);
} else {
  if (args.length === 3) {
    console.log(0);
  } else if (args.length > 3) {
    args.sort(function (a, b) {
      return b - a;
    });
    console.log(parseInt(args[1]));
  }
}
