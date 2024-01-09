#!/usr/bin/node
const args = process.argv.slice(2);
let resultat = 0;
function add (a, b) {
  resultat = a + b;
  return resultat;
}
add(parseInt(args[0]), parseInt(args[1]));
console.log(resultat);
