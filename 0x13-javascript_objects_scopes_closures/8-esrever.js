#!/usr/bin/node
exports.esrever = function (list) {
    const myReverse = [];
    for (let j = list.length - 1; j >= 0; j--) {
      myReverse.push(list[j]);
    }
    return myReverse;
  };
