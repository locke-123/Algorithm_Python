from sys import stdin as s
s = open("i.txt", "r")
n = s.readline().strip()

sum = 0
for a in n:
    sum += int(a)
print(sum)