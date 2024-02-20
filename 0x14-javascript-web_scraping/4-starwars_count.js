#!/usr/bin/node
const myrequest = require('request');

const myapiUrl = process.argv[2];

myrequest.get(myapiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const u = body.split('people/18').length - 1;
    console.log(u);
  } else {
    console.error(error);
  }
});
