from sys import stdin as s
s = open("i.txt", "r")
n = int(s.readline().strip())

for i in range(1, n+1):
    sn = str(i)
    res = ""
    for j in sn:
        if int(j) == 3:
            res += "-"
        elif int(j) == 6:
            res += "-"
        elif int(j) == 9:
            res += "-"
    if res != "":
        print(res, end=" ")
    else:
        print(i, end=" ")