function solution(n, computers) {
  let answer = 0;

  const anc = Array(n);
  for (let i = 0; i < n; i++) {
    anc[i] = i;
  }

  for (let i = 0; i < n - 1; i++) {
    for (let j = i+1; j < n; j++) {
      if (computers[i][j]) union(i, j);
    }
  }
  anc.forEach((v, i) => {if (v === i) answer++;})

  function union(x, y) {
    let ancX = find(x), ancY = find(y);
    anc[ancY] = ancX;
  }

  function find(n) {
    if (anc[n] === n) return n;
    return find(anc[n]);
  }

  return answer;
}
