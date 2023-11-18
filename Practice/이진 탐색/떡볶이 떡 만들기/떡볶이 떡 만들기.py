from sys import stdin as s
s = open("i.txt", "rt")
n, m = map(int, s.readline().split())
arr = list(map(int, s.readline().split()))

res = 0
start = 0
end = max(arr)
while end >= start:
  total = 0
  mid = (start+end)//2
  for i in arr:
    if i > mid:
      total += (i - mid)
  if total < m:
    end = mid-1
  else:
    res = mid
    start = mid+1

print(res)