import math

def power(a, b, c):
    r = 1
    while b != 0:
        if b & 1:
            r = (r * a)%c
        a = (a * a) % c
        b >>= 1
    return r

def asdf(a, b):
    global test2
    arr = [0, 1, 2]
    n = int(math.log10(a)) + b + 1
    i = 3
    if n > 2:
        while i <= n:
            if (9%i * power(10, i-2, i))%i != 0:
                tmp = (9%i * power(10, i-2, i))%i
            else:
                tmp = i
            arr_a = arr[:]
            del arr_a[tmp:]
            arr_b = [arr[tmp-1]]
            arr_c = arr[:]
            del arr_c[:tmp]
            if tmp == i:
                arr = arr_b + arr_a
            elif tmp != i:
                arr = arr_a + arr_b + arr_c
                for j in range(tmp):
                    arr_b = arr[:]
                    del arr_b[1:]
                    arr = arr[1:] + arr_b 
            i += 1

    k = power(10, n-1, n+1)
    l = (a%(n+1) * power(10, b, n+1))%(n+1)
    print(arr)       
    return test2[arr[l-k]]

T = int(input())
case = []
case2 = []
test = [-1,'1','-2', '1-3', '-2-4', '1-3-5', '-2-4-6', '1-3-5-7', '-2-4-6-8', '1-3-5-7-9', '1-3-5-7-10', '-2-4-6-8-11', '1-3-5-7-9-12', '1-3-5-7-10-13', '-2-4-6-8-11-14', '1-3-5-7-9-12-15', '1-3-5-7-10-13-16', '-2-4-6-8-11-14-17', '1-3-5-7-9-12-15-18', '1-3-5-7-10-13-16-19', '-2-4-6-8-11-14-17-20']
test2 = ['1-3-5-7-10-13-16-...', '-2-4-6-8-11-14-17...', '1-3-5-7-9-12-15-1...']
py = []
for i in range(T):
    case.append(list(map(int, input().split())))
    if case[i][1] < 2 and case[i][0] < 21 and case[i][0] * pow(10, case[i][1]) < 21:
        case2.append(case[i][0] * pow(10, case[i][1]))
    else:
        case2.append(21)

        

for i in range(T):
    if case2[i] < 21:
        py.append(test[case2[i]])

    else:
        py.append(asdf(case[i][0], case[i][1]))

for i in py:
    print(i)
