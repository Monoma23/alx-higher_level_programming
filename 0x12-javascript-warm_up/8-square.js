#!/usr/bin/node
const args = process.argv.slice(2);
let u, k;
if (isNaN(args[0])) {
  console.log('Missing size');
} else {
  for (u = 0; u < parseInt(args[0]); u++) {
    let row = '';
    for (k = 0; k < parseInt(args[0]); k++) {
      row += 'X';
    }
    console.log(row);
  }
}
