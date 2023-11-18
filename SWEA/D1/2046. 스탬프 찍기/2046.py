from sys import stdin as s
s = open("i.txt", "r")
n = int(s.readline().strip())
res = ""
for _ in range(n):
    res += "#"
print(res)