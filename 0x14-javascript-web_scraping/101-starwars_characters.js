#!/usr/bin/node

const request = require('request');

function getmyDataFrom (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, _res, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

function errorHandl (err) {
  console.log(err);
}

function displayMovieCharacters (movieId) {
  const mymovieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getmyDataFrom(mymovieUrl)
    .then(JSON.parse, errorHandl)
    .then(function (res) {
      const charcs = res.charcs;
      const mypromises = [];

      for (let v = 0; v < charcs.length; ++v) {
        mypromises.push(getmyDataFrom(charcs[v]));
      }

      Promise.all(mypromises)
        .then((results) => {
          for (let v = 0; v < results.length; ++v) {
            console.log(JSON.parse(results[v]).name);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    });
}

displayMovieCharacters(process.argv[2]);
