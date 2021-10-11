import sys

def fail(pattern):
    n = len(pattern)
    f = [0 for i in range(n)]
    begin = 1
    m = 0
    while begin + m < n:
        if pattern[begin+m] == pattern[m]:
            m += 1
            f[begin+m-1] = m
        elif pattern[begin+m] != pattern[m]:
            if m == 0:
                begin += 1
            elif m != 0:
                begin += m - f[m-1]
                m = f[m-1]
    return f

a = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()
f = fail(pattern)
a_len = len(a)
pattern_len = len(pattern)
begin = 0
m = 0
i = 0
j = 0
arr = []
count = 0
while i < a_len :
    while j and a[i] != pattern[j] :
        j = f[j-1]
    if a[i] == pattern[j] :
        if j == pattern_len -1:
            arr.append(i-pattern_len+2)
            j = f[j]
            count += 1
        else:
            j+=1
    i += 1 

# while begin + m < a_len:
#     if a[begin+m] == pattern[m]:
#         if m == pattern_len -1:
#             count += 1
#             arr.append(begin+1)
#             begin += m - f[m-1]
#             m = f[m-1]
#         else:
#             m += 1
#     else:
#         if m == 0:
#             begin += 1
#         else:
#             begin += m - f[m-1]
#             m = f[m-1]

print(count)

for i in arr:
    print(i, end= " ")