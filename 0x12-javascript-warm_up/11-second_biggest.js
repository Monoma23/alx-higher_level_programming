#!/usr/bin/node
const args = process.argv.slice(2);
if (!args[0] || !args[2]) {
  console.log(0);
} else {
  const args = args.map(Number);
  const maxima1 = Math.max.apply(null, args);
  args.splice(args.indexOf(maxima1), 1);
  console.log(Math.max.apply(null, args));
}
