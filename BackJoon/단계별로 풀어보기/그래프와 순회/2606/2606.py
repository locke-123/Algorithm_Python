from sys import stdin as s
from collections import deque
# s = open("i.txt", "r")
n = int(s.readline().strip())
m = int(s.readline().strip())
line = [ [] for _ in range(n+1)]
for _ in range(m):
  v1, v2 = map(int, s.readline().split())
  line[v1].append(v2)
  line[v2].append(v1)
visit = [False] * (n+1)
que = deque()
que.append(1)
count = -1
while que:
  t = que.popleft()
  if visit[t]:
    continue
  visit[t] = True
  count += 1
  for i in line[t]:
    if visit[i]:
      continue
    else:
      que.append(i)
print(count)