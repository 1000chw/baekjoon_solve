function solution(k, dungeons) {
  let answer = -1;

  const idx = [];
  for (let i = 0; i < dungeons.length; i++) {
    idx.push(i);
  }

  const idxPermutation = permutation(idx, idx.length);

  idxPermutation.map(idx => {
    let curK = k;
    let cnt = 0;
    for (let i = 0; i < idx.length; i++) {
      if (curK < dungeons[idx[i]][0]) {
        break;
      }
      else {
        curK -= dungeons[idx[i]][1];
        cnt++;
      }
    }
    answer = Math.max(answer, cnt);
  })

  return answer;
}

function permutation(arr, num) {
  const res = [];
  if (num === 1) return arr.map(v => [v]);

  arr.forEach((v, idx, arr) => {
    const rest = [...arr.slice(0, idx), ...arr.slice(idx + 1)];
    const permutations = permutation(rest, num - 1);
    const attach = permutations.map((permutation) => [v, ...permutation]);
    res.push(...attach)
  })
  return res;
}

console.log(solution(80, [[80,20],[50,40],[30,10]]))