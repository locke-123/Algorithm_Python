from sys import stdin as s
s = open("i.txt", "r")
n = int(s.readline().strip())
arr = list(map(int,s.readline().split()))
m = int(s.readline().strip())
marr = list(map(int,s.readline().split()))

arr.sort()
def fnum(t):
  start = 0
  end = n-1
  while end >= start:
    mid = (start+end)//2
    if arr[mid] == t:
      return 'yes'
    if arr[mid] > t:
      end = mid-1
    elif arr[mid] < t:
      start = mid+1
  return 'no'

for a in marr:
  print(fnum(a), end=" ")