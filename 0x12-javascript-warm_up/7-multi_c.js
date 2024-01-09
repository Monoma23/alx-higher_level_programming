#!/usr/bin/node
const args = process.argv.slice(2);
let k = 0;
if (isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  while (k < parseInt(args[0])) {
    console.log('C is fun');
    k++;
  }
}
