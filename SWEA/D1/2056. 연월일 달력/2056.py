from sys import stdin as s
s = open("i.txt", "r")
T = int(s.readline().strip())

for i in range(1,T+1):
    ymd = s.readline().strip()
    y = ymd[0:4]
    m = ymd[4:6]
    d = ymd[6:8]
    if int(m) > 12 or int(m) < 1:
        print("#"+str(i), -1)
        continue
    if int(d) > 31:
        print("#" + str(i), -1)
        continue
    if int(d) > 30:
        nm = int(m)
        if nm == 2 or nm == 4 or nm == 6 or nm == 9 or nm == 1:
            print("#" + str(i), -1)
            continue
    if int(d) > 28:
        if int(m) == 2:
            print("#" + str(i), -1)
            continue
    print("#"+str(i), y+"/"+m+"/"+d)