#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return ((list.filter(a => a === searchElement)).length);
};
