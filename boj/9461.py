def Pado(n):
    global dp
    if n < 6:
        return dp[n]
    
    if dp[n] != -1:
        return dp[n]
    dp[n] = Pado(n-1) + Pado(n-5)
    return dp[n]

arr = []
dp = [-1 for i in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

a = int(input())
for i in range(a):
    arr.append(int(input()))

for i in arr:
    print(Pado(i))