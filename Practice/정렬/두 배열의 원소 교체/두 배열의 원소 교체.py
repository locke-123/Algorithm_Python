from sys import stdin as s
s = open("i.txt", "rt")
n, k = map(int, s.readline().split())
A = list(map(int, s.readline().split()))
B = list(map(int, s.readline().split()))
A.sort()
B.sort(reverse=True)
for i in range(k):
  if A[i] < B[i]:
    A[i] = B[i]
  else:
    break
print(sum(A))