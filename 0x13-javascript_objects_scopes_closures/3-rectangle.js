#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h) {
      if ((w !== 0 && w > 0) && (h !== 0 && h > 0)) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    const letter = 'X';
    for (let col = 0; col < this.height; col++) {
      console.log(letter.repeat(this.width));
    }
  }
};
