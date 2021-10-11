# 숫자의 개수
arr = []
arr2 = [0 for i in range(10)]
for i in range(3):
    arr.append(int(input()))
result = str(arr[0]*arr[1]*arr[2])

for i in result:
    if int(i) == 0:
        arr2[0] += 1
    if int(i) == 1:
        arr2[1] += 1
    if int(i) == 2:
        arr2[2] += 1
    if int(i) == 3:
        arr2[3] += 1
    if int(i) == 4:
        arr2[4] += 1
    if int(i) == 5:
        arr2[5] += 1
    if int(i) == 6:
        arr2[6] += 1
    if int(i) == 7:
        arr2[7] += 1
    if int(i) == 8:
        arr2[8] += 1
    if int(i) == 9:
        arr2[9] += 1

for i in arr2:
    print(i)