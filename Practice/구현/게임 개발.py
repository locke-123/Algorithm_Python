from sys import stdin as s
s = open("i.txt", "rt")

n , m = map(int, s.readline().split())
y, x, look = map(int, s.readline().split())
gamemap = [list(map(int,s.readline().split())) for _ in range(n)]
#print(gamemap) #1 바다 0 육지

l = [[-1,0],[0,1],[1,0],[0,-1]]
count = 1
gamemap[y][x] = 2
stack = 0

def rotatel(): #무조건 왼회전
  global look
  look -= 1
  if(look < 0):
    look = 3

while True:
  print(x, y)
  if(stack == 4):
    ix = (l[look][1]*-1)+x
    iy = (l[look][0]*-1)+y
    if(ix < 0 or iy < 0 or ix >= m or iy >= n or gamemap[iy][ix] == 1):
      break
    x = ix
    y = iy
    continue
  rotatel()
  ix = l[look][1]+x
  iy = l[look][0]+y
  if(ix < 0 or iy < 0 or ix >= m or iy >= n):
    stack += 1
    continue
  if(gamemap[iy][ix] == 1 or gamemap[iy][ix] == 2):
    stack += 1
    continue
  x = ix
  y = iy
  count += 1
  gamemap[y][x] = 2
  stack = 0

print(count)