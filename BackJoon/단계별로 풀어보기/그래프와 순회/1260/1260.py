from sys import stdin as s
from collections import deque
# s = open("i.txt", "r")
n, m, f = map(int, s.readline().split())
line = [[] for _ in range(n+1)]
for _ in range(m):
  v1, v2 = map(int, s.readline().split())
  line[v1].append(v2)
  line[v2].append(v1)
for i in line:
  i.sort()

# dfs
vis = [False] * (n+1)
res = []

def dfs(t):
  global count
  global vis
  global line
  global res
  vis[t] = True
  res.append(t)

  for i in line[t]:
    if vis[i]:
      continue
    else:
      dfs(i)

dfs(f)
for i in res:
  print(i, end=' ')
print('')
#bfs
vis = [False] * (n+1)
res = []
que = deque()
que.append(f)
while que:
  t = que.popleft()
  if vis[t]:
    continue
  vis[t] = True
  res.append(t)
  for i in line[t]:
    if vis[i]:
      continue
    else:
      que.append(i)
for i in res:
  print(i, end=' ')