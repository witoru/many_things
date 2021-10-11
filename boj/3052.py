# 나머지
arr = []
count = 0
for i in range(10):
    arr.append(int(input()))
for i in range(10):
    arr[i] = arr[i] % 42
for i in range(10):
    for j in range(9-i):
        if arr[i] == arr[j + 1 + i]:
            arr [j+1+i] = arr[j+1+i] - 43

for i in arr:
    if i >= 0:
        count+=1

print(count)