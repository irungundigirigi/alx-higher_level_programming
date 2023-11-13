#!/usr/bin/node
const arg = Math.floor(Number(process.argv[2]));
console.log(isNaN(arg) ? 'Not a number' : `My number: ${arg}`);
