const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

let max_len = 0

for (let i = 0; i < input.length; i++) {
  if (max_len < input[i].length)
    max_len = input[i].length;
}

let answer = "";

for (let i = 0; i < max_len; i++) {
  for (let j = 0; j < input.length; j++) {
    if (input[j].length > i) {
      answer += input[j][i];
    }
  }
}
console.log(answer)