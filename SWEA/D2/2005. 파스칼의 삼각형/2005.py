from sys import stdin as s
s = open("i.txt", "r")
T = int(s.readline().strip())

for i in range(1, T+1):
    n = int(s.readline().strip())
    arr = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(j+1):
            if k == 0:
                arr[j][k] = 1
            elif k == j:
                arr[j][k] = 1
            else:
                arr[j][k] = arr[j-1][k-1]+arr[j-1][k]
    print("#"+str(i))
    for j in arr:
        for k in j:
            if k == 0:
                continue
            print(k, end=" ")
        print()