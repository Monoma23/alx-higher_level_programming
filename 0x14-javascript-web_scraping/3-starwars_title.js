#!/usr/bin/node
const reqq = require('request');
const urll = 'https://swapi-api.alx-tools.com/api/films/';
const myid = process.argv[2];
reqq.get(urll + myid, (error, res, body) => {
  if (!error && res.statusCode === 200) {
    const mydata = JSON.parse(body);
    console.log(mydata.title);
  } else {
    console.log(error);
  }
});
