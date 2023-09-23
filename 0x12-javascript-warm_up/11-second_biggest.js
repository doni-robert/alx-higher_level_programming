#!/usr/bin/node
const argList = process.argv.slice(2).map(arg => parseInt(arg));
if (!process.argv[2] || argList.length === 1) {
  console.log('0');
} else {
  argList.sort((a, b) => b - a);
  console.log(argList[1]);
}
