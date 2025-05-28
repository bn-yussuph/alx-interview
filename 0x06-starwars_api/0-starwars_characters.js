#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const xters = JSON.parse(body).characters;
  for (let i = 0; i < xters.length; i++) {
    request(xters[i], function (err, res, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  }
});
