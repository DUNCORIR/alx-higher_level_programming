#!/usr/bin/node

// The script for a class rectangle that defines Rectangle.
class Rectangle {
    constructor(w, h) {
        // Check if w or h is 0 or not a positive integer
        if (w <= 0 || h<= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            // if condition is met, create empty object by returning early
            return;
        }
        // Otherwise initialize object with given width and height.
        this.width = w;
        this.height = h;
    }
}

module.exports = Rectangle;