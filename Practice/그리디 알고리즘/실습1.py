n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

res = 0
i = 0
stack = 1
for _ in range(m):
  if (stack > k):
    if (i == 0):
      i = 1
      stack = k
    else:
      i = 0
      stack = 1

  res += a[i]
  print(a[i])
  stack += 1

print(res)
