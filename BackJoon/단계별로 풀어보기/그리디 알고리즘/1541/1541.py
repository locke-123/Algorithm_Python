from sys import stdin as s
# s = open("i.txt","rt")
c = list(s.readline().split('-'))
# print(c)

for i in range(len(c)):
  c[i] = sum(map(int, c[i].split('+')))
res = c[0]
for i in range(1, len(c)):
  res -= c[i]
print(res)