#!/usr/bin/node
const args = process.argv.slice(2);
if (!args[0]) {
  console.log('"undefined is undefined"');
} else {
  console.log(args[0], 'is', args[1]);
}
