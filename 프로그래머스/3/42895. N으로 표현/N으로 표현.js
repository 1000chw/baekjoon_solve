function solution(N, number) {
  let answer = -1;
  if (N === number) return 1;

  const map = new Map();
  map.set(1, [N]);

  let mult = 11;

  for (let i = 2; i < 9; i++) {
    const tmpSet = new Set([mult * N]);

    for (let j = 1; j < i; j++) {
      const calcResult = calc(map.get(j), map.get(i-j));
      calcResult.forEach(v => tmpSet.add(v));
    }
    if (tmpSet.has(number)) {
      answer = i;
      break;
    }
    map.set(i, [...tmpSet.values()]);
    mult = mult * 10 + 1;
  }

  function calc(set1, set2) {
    const set = new Set();
    for (let i = 0; i < set1.length; i++) {
     for (let j = 0; j < set2.length; j++) {
       set.add(set1[i]+set2[j]);
       set.add(set1[i]-set2[j]);
       set.add(set1[i]*set2[j]);
       set.add(Math.floor(set1[i]/set2[j]));
     }
    }
    return [...set];
  }

  return answer;
}