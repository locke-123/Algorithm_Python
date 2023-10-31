from sys import stdin as s
from collections import deque

s = open("i.txt", "rt")

n, m = map(int, s.readline().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, s.readline().strip())))
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
  global arr, visited, n, m
  que = deque()
  que.append((i, j))

  while que:
    x, y = que.popleft()
    print(x, y)
    for num in range(4):
      tx = x + dx[num]
      ty = y + dy[num]
      if (tx < 0 or tx >= n or ty < 0 or ty >= m):
        continue
      if (arr[tx][ty] == 0):
        continue
      if (arr[tx][ty] == 1):
        arr[tx][ty] = arr[x][y] + 1
        que.append((tx, ty))
  return arr[n - 1][m - 1]


print(bfs(0, 0))
for i in range(n):
  print(arr[i])
