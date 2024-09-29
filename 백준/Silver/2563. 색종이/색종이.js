let input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number))

const paper = Array.from(new Array(100), () => new Array(100).fill(0))

const n = input[0][0];

for (let i = 1; i <= n; i++) {
  const [x, y] = input[i];
  for (let j = x; j < x + 10; j++) {
    for (let k = y; k < y + 10; k++) {
      paper[j][k] = 1;
    }
  }
}

let answer = 0;

for (let i = 0; i < 100; i++) {
  for (let j = 0; j < 100; j++) {
    answer += paper[i][j];
  }
}

console.log(answer)