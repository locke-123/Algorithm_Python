from sys import stdin as s
s = open("i.txt", "r")
a, b = map(int, s.readline().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)