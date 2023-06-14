#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  while (i < list.length / 2) {
    [list[i], list[list.length - 1 - i]] = [list[list.length - 1 - i], list[i]];
    i++;
  }
  return (list);
};
