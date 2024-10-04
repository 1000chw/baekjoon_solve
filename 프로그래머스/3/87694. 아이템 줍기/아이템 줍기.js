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

function solution(rectangle, characterX, characterY, itemX, itemY) {
  let answer = 0;

  const map = Array.from(new Array(102), () => Array(102).fill(0));

  rectangle.forEach((item) => {
    const [x1, y1, x2, y2] = item.map(x => x * 2);
    for (let i = x1; i <= x2; i++) {
      for (let j = y1; j <= y2; j++) {
        if (i === x1 || i === x2 || j === y1 || j === y2) {
          if (map[i][j] !== 2) map[i][j] = 1;
        } else map[i][j] = 2;
      }
    }
  })

  bfs();

  function bfs() {
    const dx = [1,0,-1,0], dy = [0,1,0,-1];

    const visited = Array.from(new Array(102), () => Array(102).fill(false));
    const queue = new Queue();
    queue.push([characterX*2, characterY*2, 0]);

    while (queue.size()) {
      const [x, y, cnt] = queue.pop();

      if (x === itemX*2 && y === itemY*2) {
        answer = cnt;
        break;
      }

      if (visited[x][y]) continue;

      visited[x][y] = true;

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i], ny = y + dy[i];
        if (0 <= nx && 0 <= ny && !visited[nx][ny] && map[nx][ny] === 1) {
          queue.push([nx, ny, cnt + 1]);
        }
      }
    }
  }

  return answer/2;
}
