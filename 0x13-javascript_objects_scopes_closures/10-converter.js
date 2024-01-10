#!/usr/bin/node
exports.converter = function (base) {
    return function (m) {
      return m.toString(base);
    };
  };
