#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      console.log('X');
    }
  }
} else { console.log('Missing size'); }
