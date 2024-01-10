#!/usr/bin/node
const FatherSquare = require('./5-square');
module.exports = class Square extends FatherSquare {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let k = 0; k < this.width; k++) {
        row += c;
      }
      console.log(row);
    }
  }
};
