from sys import stdin as s

s = open("i.txt", "rt")

n, m = map(int, s.readline().split())  #n :row, m: col
# val = [[] for _ in range(n)]
val = []
visited = [[False] * m for _ in range(n)]

# for i in range(n):
#   rowVals = s.readline()
#   for j in range(m):
#     val[i].append(int(rowVals[j]))

for i in range(n):
  val.append(list(map(int,s.readline().strip())))

count = 0

def dfs(val, i, j, visited):
  global count
  global n
  global m
  if(visited[i][j] == False and val[i][j] == 0):
    visited[i][j] = True
    if(i+1 < n):
      dfs(val, i+1, j, visited)
    if(i-1 > -1):
      dfs(val, i-1, j, visited)
    if(j+1 < m):
      dfs(val, i, j+1, visited)
    if(j-1 > -1):
      dfs(val, i, j-1, visited)
  else:
    return


for i in range(n):
  for j in range(m):
    if(visited[i][j] == True or val[i][j] == 1):
      continue
    dfs(val, i, j, visited)
    count += 1

print(val)
print(count)