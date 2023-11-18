from sys import stdin as s
s = open("i.txt", "r")
T = int(s.readline().strip())

for i in range(1,T+1):
    a, b = map(int,s.readline().split())
    print("#"+str(i), a//b, a%b)