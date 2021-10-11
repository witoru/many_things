import sys

sys.setrecursionlimit(100000)
def Tile(n):
    global dp
    if n < 3:
        return dp[n]
    
    if dp[n] != -1:
        return dp[n]
    dp[n] = Tile(n-1) + Tile(n-2)
    return dp[n]

dp = [-1 for i in range(1001)]
dp[1] = 1
dp[2] = 2


a = int(input())
print(Tile(a) % 10007)
