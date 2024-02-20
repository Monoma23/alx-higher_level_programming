#!/usr/bin/node
const reqq = require('request');

const myurl = process.argv[2];

reqq.get(myurl, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
