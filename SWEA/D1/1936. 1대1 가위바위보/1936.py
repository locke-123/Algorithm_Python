from sys import stdin as s
s = open("i.txt", "r")
a, b = map(int, s.readline().split())
# 가위는 1, 바위는 2, 보는 3
if a == 1:
    if b == 2:
        print("B")
    elif b == 3:
        print("A")
if a == 2:
    if b == 1:
        print("A")
    elif b == 3:
        print("B")
if a == 3:
    if b == 1:
        print("B")
    elif b == 2:
        print("A")
