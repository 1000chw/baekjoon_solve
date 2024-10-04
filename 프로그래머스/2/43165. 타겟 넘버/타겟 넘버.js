function solution(numbers, target) {
  let answer = 0;
  solve(0, 0)
  function solve(ind, result) {
    if (ind === numbers.length) {
      if (result === target) {
        answer++;
      }
    } else {
      solve(ind + 1, result + numbers[ind]);
      solve(ind + 1, result - numbers[ind]);
    }
  }

  return answer;
}

