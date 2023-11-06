from sys import stdin as s
s = open("i.txt", "rt")
n = int(s.readline().strip())
arr = [int(s.readline().strip()) for _ in range(n)]
arr.sort(reverse=True)
for i in arr:
  print(i, end=' ')