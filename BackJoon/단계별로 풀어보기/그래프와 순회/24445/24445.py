from sys import stdin as s
from collections import deque
# s = open("i.txt", "r")
n, m, f = map(int, s.readline().split())
line = [[] for _ in range(n+1)]
for _ in range(m):
  v1, v2 = map(int, s.readline().split())
  line[v1].append(v2)
  line[v2].append(v1)
for i in range(n+1):
  line[i].sort(reverse = True)
visit = [False] * (n+1)
res = [0] * (n+1)
count = 1
que = deque()
que.append(f)
while que:
  t = que.popleft()
  if visit[t]:
    continue
  visit[t] = True
  res[t] = count
  # print(visit, line, t, que)
  count += 1
  for i in line[t]:
    if visit[i]:
      continue
    else:
      que.append(i)

for i in range(1,n+1):
  print(res[i])