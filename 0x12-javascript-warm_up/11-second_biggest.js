#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const array = process.argv.slice(2, process.argv.length);
  array.sort(function (a, b) { return a - b; });
  array.pop();
  const max = Math.max(...array);
  console.log(max);
}
