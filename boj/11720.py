# https://www.acmicpc.net/problem/11720
N = int(input())
m = list(input())
sum = 0
for i in range(len(m)):
    sum += int(m[i])

print(sum)