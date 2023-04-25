#!/usr/bin/node

// printing the status code of a GET request

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    const chars = data.results[i].characters;
    if (chars.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count = count + 1;
    }
  }
  console.log(count);
});
