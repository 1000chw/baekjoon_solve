function solution(numbers) {
  var answer = 0;
  let isPrime = makePrimeArray();
  let s = new Set();
  answer = makeNums(numbers, [0,0,0,0,0,0,0], '', isPrime, 0);

  return answer;
}

function makePrimeArray() {
  let isPrime = [];
  isPrime.length = 10000000;
  isPrime.fill(true);
  isPrime[0] = false;
  isPrime[1] = false;
  for (let i = 2; i < Math.sqrt(10000000) + 1; i++) {
    if (isPrime[i]) {
      for (let j = 2; j <= 10000000 / i; j++) {
        isPrime[i*j] = false;
      }
    }
  }
  return isPrime;
}

function makeNums(numbers, inds, num, isPrime, cnt) {
  if (cnt === numbers.length) {
    if (isPrime[+num]) {
      isPrime[+num] = false;
      return 1;
    }
    else return 0;
  }
  let answer = 0;
  if (isPrime[+num]) {
    answer++;
    isPrime[+num] = false;
  }
  for (let i = 0; i < numbers.length; i++) {
    if (inds[i] === 0) {
      inds[i] = 1;
      answer += makeNums(numbers, inds, num+numbers.at(i), isPrime, cnt+1);
      inds[i] = 0;
    }
  }
  return answer;
}