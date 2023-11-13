from collections import deque
from sys import stdin as s
# s = open("i.txt", "rt")
n, m, r = map(int, s.readline().split())
line = [[] for _ in range(n+1)]
for _ in range(m):
  v1, v2 = map(int, s.readline().split())
  line[v1].append(v2)
  line[v2].append(v1)
for i in range(n+1):
  line[i].sort()
visit = [False] * (n+1)
queue = deque()
res = [0] * (n+1)
visit[r] = True
queue.append(r)
count = 1
while queue:
  u = queue.popleft()
  res[u] = count
  count += 1
  for i in line[u]:
    if visit[i]:
      continue
    else:
      visit[i] = True
      queue.append(i)
for i in range(1,n+1):
  print(res[i])