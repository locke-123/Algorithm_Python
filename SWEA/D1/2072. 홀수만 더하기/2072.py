from sys import stdin as s
s = open("i.txt", "r")
T = int(s.readline().strip())

for i in range(1,T+1):
    arr = list(map(int, s.readline().split()))
    sum = 0
    for n in arr:
        if n%2 != 0:
            sum += n
    print("#"+str(i), sum)