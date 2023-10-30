from sys import stdin as s
s = open("input.txt", "rt")

n, m = map(int, s.readline().split())
arr = [list(map(int, s.readline().split())) for _ in range(n)]

rowmin = []
for i in range(n):
  rowmin.append(min(arr[i]))
print(max(rowmin))