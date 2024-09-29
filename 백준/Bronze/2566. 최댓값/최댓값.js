let input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number))

let max_x = 1;
let max_y = 1;
let max_n = 0;

for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (input[i][j] > max_n) {
      max_x = i+1;
      max_y = j+1;
      max_n = input[i][j];
    }
  }
}
console.log(max_n)
console.log(max_x, max_y)
