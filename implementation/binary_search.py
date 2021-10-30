import random

arr = list(range(10000))
a = int(input())
mx = len(arr) - 1
mn = 0
while mn < mx:
    mid = (mn + mx) // 2
    if a > arr[mid]:
        mn = mid + 1
    else:
        mx = mid

if a == mn:
    print(a)
else:
    print(0)