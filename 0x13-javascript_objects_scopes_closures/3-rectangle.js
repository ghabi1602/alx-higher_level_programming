#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let ch;
    for (let i = 0; i < this.height; i++) {
      ch = '';
      for (let j = 0; j < this.width; j++) {
        ch += 'X';
      }
      console.log(ch);
    }
  }
}
module.exports = Rectangle;
