from sys import stdin as s
s = open("i.txt", "r")
T = int(s.readline().strip())

for i in range(1, T+1):
    n = int(s.readline().strip())
    arr = list(map(int,s.readline().split()))
    mn = arr[n-1]
    sum = 0
    for j in range(n-2, -1, -1):
        if mn < arr[j]:
            mn = arr[j]
        else:
            sum += mn-arr[j]
    print("#"+str(i), sum)

# from sys import stdin as s
#
# s = open("i.txt", "r")
# T = int(s.readline().strip())
# arr = []
# bag = []
#
# for i in range(1, T + 1):
#     n = int(s.readline().strip())
#     arr = list(map(int, s.readline().split()))
#     bag.clear()
#     res = 0
#     mn = max(arr)
#     for m in range(len(arr)):
#         if arr[m] == mn:
#             for j in bag:
#                 res += arr[m] - j
#             if m + 1 >= n: continue
#             mn = max(arr[m + 1:])
#             # print(arr[m+1:])
#             bag.clear()
#         else:
#             bag.append(arr[m])
#     print("#" + str(i), res)