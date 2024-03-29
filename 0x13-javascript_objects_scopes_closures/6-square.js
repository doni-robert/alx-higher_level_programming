#!/usr/bin/node
const newSquare = require('./5-square');

module.exports = class Square extends newSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { this.print(); } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
