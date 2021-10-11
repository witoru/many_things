# 음계
arr = list(map(int, input().split()))
acount = 0
dcount = 0
for i in range(8):
    if arr[i] == i+1:
        acount += 1
    if arr[i] == 8-i:
        dcount += 1
if acount == 8:
    print('ascending')
elif dcount == 8:
    print("descending")
else:
    print("mixed")
