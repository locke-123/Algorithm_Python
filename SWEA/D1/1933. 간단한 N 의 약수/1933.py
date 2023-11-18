from sys import stdin as s
s = open("i.txt", "r")
n = int(s.readline().strip())
res = []

for i in range(1, n+1):
    if n%i == 0:
        res.append(i)

for i in res:
    print(i, end=" ")