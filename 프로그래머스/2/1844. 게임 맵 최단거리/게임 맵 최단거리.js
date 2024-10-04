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


function solution(maps) {
  let answer = -1;
  const mapX = maps.length, mapY = maps[0].length;

  bfs();

  function bfs() {
    const dx = [1, 0, -1, 0], dy = [0, 1, 0, -1];
    const visited = Array.from(new Array(mapX), () => new Array(mapY).fill(false));
    const queue = new Queue();
    queue.push([0, 0, 1]);

    while (queue.size()) {
      const [x, y, cnt] = queue.pop();
      if (visited[x][y]) continue;
      if (x === mapX - 1 && y === mapY - 1) {
        answer = cnt;
        break;
      }
      visited[x][y] = true;
      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i], ny = y + dy[i];
        if (0 <= nx && nx < mapX && 0 <= ny && ny < mapY && maps[nx][ny] && !visited[nx][ny])
          queue.push([nx, ny, cnt+1]);
      }
    }
  }

  return answer;
}