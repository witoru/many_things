import math
import sys

def remain(a, b, c):
    r = 1
    while b != 0:
        if b & 1:
            r = (r * a)%c
        a = (a * a) % c
        b >>= 1
    return r

def pow1(a, b):
    r = 1
    while b != 0:
        if b & 1:
            r = r * a
        a = a * a
        b >>= 1
    return r

def asdf(a, b):
    global test2
    global arr
    n = int(math.log10(a)) + b + 1
    global h
    global count
    if h <= n:
        while h <= n:
            arr[h].append(arr[h][len(arr[h]) -1])
            re = (9%(h+1) * remain(10, h-1, h+1))%(h+1) -1
            if re < 0:
                re += (h+1)
            arr[h] = arr[h][re:] + arr[h][:re]
            h += 1
            arr.append(arr[h-1][:])
    arr_re = arr[n][:]
    re = remain(10, n, n+1)
    if  re == 0:
        k = n
    else:
        k = re - 1
    arr_re = arr_re[n-k:] + arr_re[:n-k]

    return test2[arr_re[((a%(n+1))*remain(10, b, n+1))%(n+1)]]
h = 3
T = int(input())
case = []
case2 = []
arr = [[],[], [0, 1, 2], [0, 1, 2]]
test = [-1,'1','-2', '1-3', '-2-4', '1-3-5', '-2-4-6', '1-3-5-7', '-2-4-6-8', '1-3-5-7-9', '1-3-5-7-10', '-2-4-6-8-11', '1-3-5-7-9-12', '1-3-5-7-10-13', '-2-4-6-8-11-14', '1-3-5-7-9-12-15', '1-3-5-7-10-13-16', '-2-4-6-8-11-14-17', '1-3-5-7-9-12-15-18', '1-3-5-7-10-13-16-19', '-2-4-6-8-11-14-17-20']
test2 = ['1-3-5-7-10-13-16-...', '-2-4-6-8-11-14-17...', '1-3-5-7-9-12-15-1...']
py = [0 for _ in range(T)]
for i in range(T):
    case.append(list(map(int, sys.stdin.readline().split())))
    if case[i][0] * pow1(10, case[i][1]) < 21 :
        case2.append(case[i][0] * pow1(10, case[i][1]))
    else:
        case2.append(21)

        

for i in range(T):
    if case2[i] < 21:
        py[i] = test[case2[i]]
    else:
        py[i] = asdf(case[i][0], case[i][1])

for i in py:
    print(i)
