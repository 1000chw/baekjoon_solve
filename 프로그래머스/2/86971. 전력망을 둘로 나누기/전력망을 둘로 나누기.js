function solution(n, wires) {
  let answer = n;
  const tree = makeTree(n, wires);
  const count = new Array(n+1).fill(0);
  countChildren(tree, count, 1);

  count.forEach(c => {
      answer = Math.min(answer, Math.abs(n - c * 2));
    }
  )

  return answer;
}

function makeTree(n, wires) {
  const connections = Array.from(Array(n+1), () => []);
  wires.forEach(wire => {
    connections[wire[0]].push(wire[1]);
    connections[wire[1]].push(wire[0]);
  })

  const tree = Array.from(Array(n+1), () => []);
  const stack = [1];
  while (stack.length) {
    const node = stack.pop();
    connections[node].forEach(next => {
      if (tree[next].length === 0) {
        stack.push(next);
        tree[node].push(next);
      }
    })
  }
  return tree;
}

function countChildren(tree, count, node) {
  count[node]++;

  if (tree[node].length === 0) return;

  tree[node].forEach(next => {
    countChildren(tree, count, next);
    count[node] += count[next];
  })
}