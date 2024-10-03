function solution(brown, yellow) {
  let answer = [];
  const sum = brown + yellow;
  for (let i = 3; i < Math.sqrt(sum) + 1; i++) {
    if (sum % i === 0) {
      const j = sum / i;
      if (i * 2 + j * 2 - 4 === brown) {
        return [j, i]
      }
    }
  }
}