from sys import stdin as s
s = open("i.txt", "r")
T = int(s.readline().strip())

for i in range(1,T+1):
    arr = list(map(int, s.readline().split()))
    res = max(arr)
    print("#"+str(i), res)