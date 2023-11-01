from sys import stdin as s
# s = open("i.txt", "rt")
n = int(s.readline().strip())
arr = list(map(int, s.readline().split()))
arr.sort()
# print(arr)
for i in range(1, n):
  arr[i] += arr[i-1]

# print(arr)
print(sum(arr))