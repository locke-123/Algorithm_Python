from sys import stdin as s

s = open("input.txt", "rt")

n = int(s.readline().strip())
arr = []
for _ in range(n):
  arr.append(list(map(int, s.readline().strip().split())))

arr = sorted(arr, key = lambda a: (a[1], a[0]))
#print(arr)
cur = arr[0][1]
count = 1
for i in range(1,n):
  if(arr[i][0] >= cur):
    count += 1
    cur = arr[i][1]
print(count)
# 0 6
# 1 4  --
# 2 13
# 3 5
# 3 8
# 5 7  --
# 5 9
# 6 10
# 8 11 -- 
# 8 12
# 12 14 --