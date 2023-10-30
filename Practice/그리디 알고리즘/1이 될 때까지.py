from sys import stdin as s
s = open("i.txt","rt")

n, k = map(int, s.readline().split())

c = 0
while n != 1:
  if n%k == 0:
    n = n/k
    c += 1
  else :
    n -= 1
    c += 1
print(c)