N = int(input())
arr = list(map(int, input().split()))
Max = max(arr)
che = [True for _ in range(Max+1)]
che[0] = False
che[1] = False
count = 0
for i in range(Max + 1):
    if che[i] == True:
        j = 2
        while i*j < Max + 1:
            che[i*j] = False
            j += 1

for i in arr:
    if che[i] == True:
        count += 1

print(count)