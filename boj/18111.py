import sys
input=sys.stdin.readline

N, M, B = map(int, input().split())
arr = []
ma = 0
mi = 256
rm = 0
st = 0
time_height = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    if mi > min(arr[i]):
        mi = min(arr[i])
    if ma < max(arr[i]):
        ma = max(arr[i])

for a in range(mi, ma+1):
    for i in range(N):
        for j in range(M):
            if arr[i][j] - a > 0:
                rm += (arr[i][j] - a)
            else:
                st += (arr[i][j] - a)
    if -1 * (rm + st) > B:
        rm = 0
        st = 0
        continue
    else:
        time_height.append([(rm*2 + abs(st)), a])
        rm = 0
        st = 0

time = time_height[0][0]
height = time_height[0][1]
for i in range(1, len(time_height)):
    if time >= time_height[i][0]:
        time = time_height[i][0]
        height = time_height[i][1]

print("%d %d" %(time, height))