def getfail(P):
    n = len(P)
    i = 1
    j = 0
    f = [0 for _ in range(n)]
    while i < n:
        while j and P[i] != P[j]:
            j = f[j - 1]
        if P[i] == P[j]:
            j += 1
            f[i] = j
        i += 1
    return f

def pow1(a, b):
    r = 1
    while b != 0:
        if b & 1:
            r = r * a
        a = a * a
        b >>= 1
    return r

def fibo(n):
    global dp
    if dp[n] != -1:
        return dp[n]
    dp[n] = (fibo(n-1) << len(str(format(fibo(n-2), 'b')))) + fibo(n-2)
    return dp[n]
    
dp = [0, 1] + [-1 for i in range(99)]
n = int(input())
print(fibo(n))
