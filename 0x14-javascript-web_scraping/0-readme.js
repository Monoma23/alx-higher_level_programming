#!/usr/bin/node

const Myfs = require('fs');

const myfile = process.argv[2];

Myfs.readFile(myfile, (err, data) => {
  if (data) {
    console.log(data.toString());
  } else {
    console.log(err);
  }
});
