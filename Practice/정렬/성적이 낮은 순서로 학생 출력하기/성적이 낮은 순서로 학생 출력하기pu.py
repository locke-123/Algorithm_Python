from sys import stdin as s
s = open("i.txt", "rt")
n = int(s.readline().strip())
arr = []
for _ in range(n):
  name, score = s.readline().split()
  score = int(score)
  arr.append((name,score))
sArr = sorted(arr, key=lambda x: x[1])
for i in sArr:
  print(i[0], end=' ')