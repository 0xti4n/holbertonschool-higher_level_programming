#!/usr/bin/node

const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      const letter = 'C';
      for (let col = 0; col < this.height; col++) {
        console.log(letter.repeat(this.width));
      }
    }
  }
};
