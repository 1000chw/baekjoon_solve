class Queue {
  constructor() {
    this.store = {};
    this.front = 0;
    this.rear = 0;
  }

  size() {
    if (this.store[this.rear] === undefined) {
      return 0;
    } else {
      return this.rear - this.front + 1;
    }
  }

  push(value) {
    if (this.size() === 0) {
      this.store['0'] = value;
    } else {
     this.rear += 1;
     this.store[this.rear] = value;
    }
  }

  pop() {
    let tmp;
    if (this.front === this.rear) {
      tmp = this.store[this.front];
      delete this.store[this.front];
      this.front = 0;
      this.rear = 0;
      return tmp;
    } else {
      tmp = this.store[this.front];
      delete this.store[this.front];
      this.front += 1;
      return tmp;
    }
  }
}


function solution(begin, target, words) {
  let answer = 0;
  
  bfs();

  function bfs() {
    const queue = new Queue();
    const visited = new Map()
    words.forEach(word => {visited.set(word, false);});
    visited.set(begin, false);
    queue.push([begin, 0]);

    while (queue.size()) {
      const [s, cnt] = queue.pop();
      if (s === target) {
        answer = cnt;
        break;
      }
      if (visited.get(s)) continue;
      visited.set(s, true);
      for (let i = 0; i < words.length; i++) {
        if (canChange(s, words[i]) && !visited.get(words[i])) {
          queue.push([words[i], cnt+1]);
        }
      }
    }
  }

  function canChange(s1, s2) {
    let diff = 0;
    for (let i = 0; i < s2.length; i++) {
      if (s1.charAt(i) !== s2.charAt(i)) {
        diff++;
      }
    }
    return diff === 1;
  }

  return answer;
}
