arr = []
sum = 0
a = 0
for i in range(9):
    arr.append(int(input()))

for j in range(8):
    for k in range(j+1 , 9):
        for l in arr:
            sum += l
        sum = sum - arr[j] - arr[k]
        if sum == 100:
            arr.remove(arr[j])
            arr.remove(arr[k-1])
            arr.sort()
            a += 1
            for m in arr:
                print(m)
            break 
        sum = 0
        
    if a == 1:
            break