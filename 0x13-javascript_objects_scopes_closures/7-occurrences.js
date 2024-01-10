#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let j = 0; j < list.length ; j++) {
    if (list[j] == searchElement){
      counter += 1;
    }
  }
  return counter;
};
