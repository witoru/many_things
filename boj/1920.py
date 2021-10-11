def BS(arr, i):
    Max = len(arr) - 1
    Min = 0
    mid = Max//2
    while Max - Min > 1:
        if arr[mid] > i:
            Max = mid       
            mid = (Max + Min)//2
        elif arr[mid] < i:
            Min = mid
            mid = (Max + Min)//2
        else:
            return 1
    if arr[Max] == i or arr[Min] == i:
        return 1
    return 0
        
N = int(input())
arrA = sorted(list(map(int, input().split())))
M = int(input())
arrB = list(map(int, input().split()))
arrS = []

for i in arrB:
    arrS.append(BS(arrA, i))

for i in arrS:
    print(i)