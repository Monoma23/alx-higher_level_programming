#!/usr/bin/node
const request = require('request');
const myid = process.argv[2];

const myurl = 'https://swapi-api.hbtn.io/api/films/';

request.get(myurl + myid, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const mydata = JSON.parse(body);
    const mycharac = mydata.characters;
    for (const perr of mycharac) {
      request.get(perr, (err, res, body) => {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(body).name);
      });
    }
  } else {
    console.log(err);
  }
});
