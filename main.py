from sys import stdin as s
# s = open("i.txt","rt")
n, m, f = map(int, s.readline().split())
line = [[] for _ in range(n+1)]
for _ in range(m):
  i, v = map(int, s.readline().split())
  line[i].append(v)
for i in range(len(line)):
  line[i].sort()
# print(line)
visited = [False] * (n+1)
res = [0] * (n+1)
count = 1
# print(visited)
stack = []
def dfs(v):
  global count
  global visited
  global res
  visited[v] = True
  res[v] = count
  count += 1
  for i in range(len(line[v])):
    if(visited[line[v][i]] == True):
      continue
    dfs(line[v][i])

dfs(f)
# print(res)
for i in range(1, len(res)):
  print(res[i])