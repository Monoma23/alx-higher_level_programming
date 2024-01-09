#!/usr/bin/node
const args = process.argv.slice(2);
function factorial (numero) {
  if (isNaN(args[0])) {
    return 1;
  }
  if (numero <= 1) {
    return 1;
  }
  return numero * factorial(numero - 1);
}
console.log(factorial(parseInt(args[0])));
