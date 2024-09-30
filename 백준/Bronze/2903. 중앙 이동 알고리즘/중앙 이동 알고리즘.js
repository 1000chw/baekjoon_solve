let n = +require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()

let x = 2;
let cell = 1;

for (let i = 0; i < n; i++) {
  x += cell;
  cell *= 2;
}
console.log(x*x)
