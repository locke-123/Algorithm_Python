from sys import stdin as s
import sys
sys.setrecursionlimit(10 ** 6)
# s = open("i.txt", "rt")
n, m, f = map(int, s.readline().split())
line = [[] for _ in range(n+1)]
for _ in range(m):
  v1, v2 = map(int, s.readline().split())
  line[v1].append(v2)
  line[v2].append(v1)
for i in range(1, n+1):
  line[i].sort(reverse = True)
# print(line)
visit = [False]*(n+1)
res = [0]*(n+1)
count = 1

def dfs(v):
  global visit
  global res
  global count
  visit[v] = True
  res[v] = count
  count += 1
  for i in range(len(line[v])):
    if (visit[line[v][i]] == True):
      continue
    dfs(line[v][i])

dfs(f)
# print(res)
for i in range(1,len(res)):
  print(res[i])