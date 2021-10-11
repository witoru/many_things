N = int(input())
arr = sorted(list(map(int, input().split())))
a = [0]
sum = 0
j = 0
for i in arr:
    a.append(a[j] + i)
    sum += a[j+1]
    j += 1


print(sum)