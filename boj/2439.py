# 별 찍기 - 2
N = int(input())
for i in range(N):
    a = '*'*(i+1)
    print(a.rjust(N))