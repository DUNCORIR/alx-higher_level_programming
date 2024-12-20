#!/usr/bin/node

// Script that defines a square and inherits from Square of 5-square.js.
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    // 'X' as the default character if c is undefined
    const charToPrint = c || 'X';
    // Loop throu' height and print character for each row.
    for (let i = 0; i < this.height; i++) {
      console.log(charToPrint.repeat(this.width));
    }
  }
}
module.exports = Square;
