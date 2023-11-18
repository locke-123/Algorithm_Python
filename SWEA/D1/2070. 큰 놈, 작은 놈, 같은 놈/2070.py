from sys import stdin as s
s = open("i.txt", "r")
T = int(s.readline().strip())

for i in range(1,T+1):
    n1, n2 = map(int, s.readline().split())
    if n1 > n2:
        res = ">"
    elif n1 == n2:
        res = "="
    else:
        res = "<"
    print("#"+str(i), res)