N, M = map(int, input().split())
arr = (list(map(int, input().split())))

start = 0
end = max(arr)
mid = (start+end)//2
count = 0

while end - start > 1:
    for i in arr:
        if i-mid > 0:
            count += (i-mid)
    if count > M:
        start = mid
        mid = (start + end)//2
    elif count < M:
        end = mid
        mid = (start + end)//2
    else:
        start = mid
        end = mid
        count = 0
        break
    count = 0

for i  in arr:
    if i-mid > 0:
        count += i-end
    
if count > M:
    print(end)
else:
    print(start)