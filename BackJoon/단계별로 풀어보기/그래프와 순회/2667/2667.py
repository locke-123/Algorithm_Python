from sys import stdin as s
from collections import deque
# s = open("i.txt", "r")
n = int(s.readline().strip())
arr = []
for _ in range(n):
  arr.append(s.readline().strip())
# print(arr)

vis = [[False] * (n) for _ in range(n)]
total = 0
near = [(-1,0),(0,1),(1,0),(0,-1)]
res = []
for i in range(n):
  for j in range(n):
    if vis[i][j] == True:
      continue
    if arr[i][j] == '0':
      continue
    total += 1
    count = 0
    que = deque()
    que.append((i,j))
    while que:
      v1, v2 = que.popleft()
      if vis[v1][v2] == True:
        continue
      vis[v1][v2] = True
      count += 1
      for t in near:
        m1, m2 = t
        m1 += v1
        m2 += v2
        if m1 >= n or m1 < 0 or m2 >= n or m2 < 0:
          continue
        if vis[m1][m2] == True:
          continue
        if arr[m1][m2] == '1':
          que.append((m1,m2))
    res.append(count)
print(total)
res.sort()
for i in res:
  print(i)