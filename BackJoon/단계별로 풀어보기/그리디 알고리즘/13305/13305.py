from sys import stdin as s
# s = open("i.txt", "rt")

n = int(s.readline().strip())
road = list(map(int, s.readline().split()))
cost = list(map(int, s.readline().split()))
cost.pop()
minicost = min(cost)
currentmin = 1000000001
total = 0
for i in range(len(cost)):
  if(cost[i] < currentmin):
    currentmin = cost[i]
  total += currentmin * road[i]
print(total)