from sys import stdin as s

#s = open("input.txt","rt")

n, k = map(int, s.readline().strip().split())
money = []
for _ in range(n):
  money.append(int(s.readline().strip()))

count = 0
i = -1

while k != 0:
  if (k // money[i] != 0):
    count += k // money[i]
    k = k % money[i]
    i -= 1
  else:
    i -= 1

print(count)
