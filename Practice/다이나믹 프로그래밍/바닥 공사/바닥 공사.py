from sys import stdin as s
s = open("i.txt", "rt")
n = int(s.readline().strip())

dp = [0 for _ in range(4+1)]

dp[1] = 1
dp[2] = dp[2-1]+2
dp[3] = dp[3-1]+dp[3-2]*2
dp[4] = dp[4-1]+dp[4-2]*2
print(dp[4])