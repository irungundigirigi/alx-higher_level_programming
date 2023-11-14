#!/usr/bin/node

exports.esrever = function (arr) {
  return arr.reduceRight(function (reversed, current) {
    reversed.push(current);
    return reversed;
  }, []);
};
