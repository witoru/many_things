arr = []
arr.append(list(map(int, input().split())))
while arr[len(arr) - 1] != [0, 0, 0]:
    arr.append(list(map(int, input().split())))

arr.pop()
for i in range(len(arr)):
    arr[i].sort()
    if pow(arr[i][0], 2) + pow(arr[i][1], 2) == pow(arr[i][2], 2):
        print("right")
    else:
        print("wrong")
