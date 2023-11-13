#!/usr/bin/node

function factorial(n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}

const input = Number(process.argv[2]);
const result = factorial(input);

console.log(result);

