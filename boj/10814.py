N = int(input())
arr = []
for i in range(N):
    arr.append(list(input().split()))
    arr[i][0] = int(arr[i][0])

arr.sort(key = lambda arr : arr[0])
print(arr)