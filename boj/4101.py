arr = []
a = -1
b = -1
while a != 0 and b != 0:
    a, b = map(int, input().split())
    arr.append([a, b])
arr.pop()
for ar in arr:
    if ar[0] > ar[1]:
        print("Yes")
    else:
        print("No")