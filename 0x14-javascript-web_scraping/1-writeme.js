#!/usr/bin/node
const fs = require('fs');

const myfile = process.argv[2];
const mycontent = process.argv[3];

fs.writeFile(myfile, mycontent, (err, data) => {
  if (err) {
    console.log(err);
  }
});
