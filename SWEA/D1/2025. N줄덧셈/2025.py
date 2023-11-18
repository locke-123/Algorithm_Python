from sys import stdin as s
s = open("i.txt", "r")
n = int(s.readline().strip())

sum = 0

for i in range(1, n+1):
    sum += i
print(sum)