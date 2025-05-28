#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const xters = JSON.parse(body).characters;
  extract(xters, 0);
});
const extract = (xters, x) => {
  if (x === xters.length) return;
  request(xters[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    extract(xters, x + 1);
  });
};
