from sys import stdin as s
s = open("i.txt", "rt")
n = int(s.readline().strip())

dp = [0 for _ in range(30001)]
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 1
for i in range(6,n+1):
  if i%2 == 0:
    a = dp[i//2]
  else:
    a = 30005
  if i%3 == 0:
    b = dp[i//3]
  else:
    b = 30005
  if i%5 == 0:
    c = dp[i//5]
  else:
    c = 30005
  dp[i] = min(a,b,c,dp[i-1])+1
print(dp[n])