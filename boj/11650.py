N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda a: a[1])
arr.sort(key = lambda b: b[0])

for i in arr:
    print("%d %d" %(i[0], i[1]))