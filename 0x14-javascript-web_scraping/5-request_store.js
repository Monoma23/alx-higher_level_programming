#!/usr/bin/node
const fs = require('fs');
const reqq = require('request');

const urll = process.argv[2];
const myfilePath = process.argv[3];

reqq.get(urll, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const fileStream = fs.createWriteStream(myfilePath);
    fileStream.write(body);
  } else {
    console.log(err);
  }
});
