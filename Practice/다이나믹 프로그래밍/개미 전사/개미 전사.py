from sys import stdin as s
s = open("i.txt", "rt")
n = int(s.readline().strip())
arr = list(map(int, s.readline().split()))

dp = [0 for _ in range(n)]

dp[0] = arr[0]
dp[1] = arr[1]
dp[2] = max(arr[0]+arr[2], arr[1])
dp[3] = max(dp[2], arr[3]+dp[1])
print(dp)

# 3 4 5 1 1 2
# 3 4 8 8