N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda a : (a[1], a[0]))

for ar in arr:
    print("%d %d" %(ar[0], ar[1]))