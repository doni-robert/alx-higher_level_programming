#!/usr/bin/node
let times = parseInt(process.argv[2]);
if (times) {
  while (times > 0) {
    console.log('C is fun');
    times--;
  }
} else { console.log('Missing number of occurrences'); }
