def fail(pattern):
    n = len(pattern)
    f = [0 for _ in range(n)]
    begin = 1
    m = 0
    while begin < n:
        while m and pattern[begin] != pattern[m]:
            m = pattern[m-1]
        if pattern[begin] == pattern[m]:
            m += 1
            f[begin] = m
        begin += 1
    return f

a = input()
pattern = input()
f = fail(pattern)
begin = 0
m = 0
count = 0
while begin + m < len(a):
    if a[begin+m] == pattern[m]:
        if m == len(pattern)-1:
            count += 1
            print(begin)
            begin += m - f[m-1]
            m = f[m-1]
        else:
            m += 1
    elif a[begin+m] != pattern[m]:
        if m == 0:
            begin += 1
        else:
            begin += m - f[m-1]
            m = f[m-1]

print(count)