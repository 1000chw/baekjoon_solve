function solution(numbers, target) {
  return solve(numbers, target, 0, 0);
}

function solve(numbers, target, ind, result) {
  if (ind === numbers.length) {
    if (result === target) {
      return 1;
    }
    return 0;
  }
  return solve(numbers, target, ind+1, result + numbers[ind]) + solve(numbers, target, ind+1, result - numbers[ind]);
}