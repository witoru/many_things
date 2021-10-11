# 문자열 반복
T = int(input())
arr = []
for i in range(T):
    arr.append(list(map(str, input().split())))
    arr[i][0] = int(arr[i][0])

for i in range(len(arr)):
    for j in arr[i][1]:
        print(j*arr[i][0], end = '')
    print()