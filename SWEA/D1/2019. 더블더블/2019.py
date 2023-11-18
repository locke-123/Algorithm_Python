from sys import stdin as s
s = open("i.txt", "r")
n = int(s.readline().strip())

for i in range(0, n+1):
    print(2**i, end=" ")