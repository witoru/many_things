# 최댓값
arr = []
for i in range(9):
    arr.append(int(input()))

Max = 0
for i in arr:
    if Max < i:
        Max = i

print(Max, arr.index(Max)+1)
