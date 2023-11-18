from sys import stdin as s
s = open("i.txt", "r")
T = int(s.readline().strip())

for i in range(1, T+1):
    p = s.readline().strip()
    a = p[0]
    for j in range(1, len(p)):
        # print(p[j:j+len(a)], a)
        if p[j:j+len(a)] == a:
            break
        a += p[j]
    print("#"+str(i), len(a))