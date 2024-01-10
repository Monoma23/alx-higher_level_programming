#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (h <= 0) || !h || !w) {
        return this;
      }
    this.width = w;
    this.height = h;
  }
  
  print () {
    for (let k = 0; k < this.height; k++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
