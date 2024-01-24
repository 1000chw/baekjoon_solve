import sys
from collections import defaultdict
input = sys.stdin.readline

graph = defaultdict(list)
time = defaultdict(int)
work_time = defaultdict(int)
count = defaultdict(int)
visited = defaultdict(bool)
start = []
while True:
    task = input().split()
    if not task:
        break
    time[task[0]] = int(task[1])
    if len(task) == 3:
        for c in task[2]:
            graph[c].append(task[0])
        count[task[0]] += len(task[2])
    else:
        start.append(task[0])
        work_time[task[0]] = int(task[1])

while start:
    task = start.pop(0)
    if count[task] != 0:
        start.append(task)
    elif visited[task]:
        continue
    else:
        visited[task] = True
        for c in graph[task]:
            work_time[c] = max(work_time[c], work_time[task] + time[c])
            count[c] -= 1
            start.append(c)

print(max(work_time.values()))
