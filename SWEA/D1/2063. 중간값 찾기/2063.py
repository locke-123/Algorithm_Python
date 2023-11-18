from sys import stdin as s
s = open("i.txt", "r")
T = int(s.readline().strip())

arr = list(map(int, s.readline().split()))
arr.sort()
res = arr[T//2]
print(res)