k, n = map(int, input().split())

lan = []
for i in range(k):
    lan.append(int(input()))
count = 0
Min = 1
Max = max(lan)
mid = (Min + Max)/2

while 1:
    for i in lan:
        count += i // mid
    if int(Max) - int(Min) > 0:
        if count < n:
            Max = mid
            mid = (Min + mid)/2
        elif  count >= n:
            Min = mid
            mid = (Max + mid)/2
    else:
        break
    count = 0
print(int(mid))
