from sys import stdin as s
s = open("i.txt", "r")
n, m = map(int,s.readline().split())

count = 0
for i in range(m, n+1):
    count += 1
print(count)