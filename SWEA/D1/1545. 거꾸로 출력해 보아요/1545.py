from sys import stdin as s
s = open("i.txt", "r")
n = int(s.readline().strip())

for i in range(n, -1, -1):
    print(i, end=" ")