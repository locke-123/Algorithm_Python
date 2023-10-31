from sys import stdin as s
s = open("i.txt", "rt")

rows = ['a','b','c','d','e','f','g','h']
c = s.readline()
row = c[0]
col = int(c[1])-1

for i in range(len(rows)):
  if(row == rows[i]):
    row = i
    break

print(row, col)
count = 0

if(row+2 < 8):
  if(col+1 < 8):
    print('q')
    count += 1
  if(col-1 > -1):
    print('w')
    count += 1
if(row-2 > -1):
  if(col+1 < 8):
    print('e')
    count += 1
  if(col-1 > -1):
    print('r')
    count += 1

if(col+2 < 8):
  if(row+1 < 8):
    print('s')
    count += 1
  if(row-1 > -1):
    print('t')
    count += 1
if(col-2 > -1):
  if(row+1 < 8):
    print('y')
    count += 1
  if(row-1 > -1):
    print('u')
    count += 1

print(count)