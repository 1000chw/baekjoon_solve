let input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number)

const n = input[0];

for (let i = 1; i <= n; i++) {
  let x = input[i];
  const change = {
    quater: 0,
    dime: 0,
    nickel: 0,
    penny: 0
  }

  change.quater = Math.floor(x / 25);
  x -= change.quater * 25;
  change.dime = Math.floor(x / 10);
  x -= change.dime * 10;
  change.nickel = Math.floor(x / 5);
  x -= change.nickel * 5;
  change.penny = x;
  console.log(change.quater, change.dime, change.nickel, change.penny);
}
