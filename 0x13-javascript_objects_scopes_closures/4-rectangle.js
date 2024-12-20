#!/usr/bin/node

// An instance print() that prints the rectangle using the character X.
// An instance method called rotate() that exchanges the width and the height of the rectangle.
// An instance method called double() that multiples the width and the height of the rectangle by 2.
class Rectangle {
  constructor (w, h) {
    // Check if w or h is 0 or not a positive integer
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // if condition is met, create empty object by returning early
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width)); // Print a row of X.
      }
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
