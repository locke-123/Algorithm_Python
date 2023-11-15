from sys import stdin as s
from collections import deque

s = open("i.txt", "r")
T = int(s.readline().strip())
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for _ in range(1):
  m, n, k = map(int, s.readline().split())
  arr = [[0] * m for _ in range(n)]
  for _ in range(k):
    v1, v2 = map(int, s.readline().split())
    arr[v2][v1] = 1
  vis = [[False] * m for _ in range(n)]
  total = 0
  for p in arr:
    print(p)
  for i in range(n):
    for j in range(m):
      if arr[i][j] == 0:
        continue
      if vis[i][j] == True:
        continue
      que = deque()
      que.append((i, j))
      while que:
        v1, v2 = que.popleft()
        if vis[v1][v2] == True:
          continue
        vis[v1][v2] = True
        total += 1
        for l in move:
          m1, m2 = l
          m1 += v1
          m2 += v2
          if m1 >= n or m1 < 0 or m2 >= m or m2 < 0:
            continue
          if vis[m1][m2] == True:
            continue
          if arr[m1][m2] == 0:
            continue
          que.append((m1, m2))
          print(m1, m2)
    for p in vis:
      print(p)
  print(total)
