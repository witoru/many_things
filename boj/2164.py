def pow(a, b):
    r = 1
    while b != 0:
        if b & 1:
            r = r * a
        a = a * a
        b >>= 1
    return r

N = int(input())

i = 0
start = 1
end = N
cd = pow(2, i) 
key = 1

while start + cd <= N:
    if (((end - start)//cd) + 1)%2 == 1:
        key_b = -1
    else:
        key_b = 1
    if key == 1:
        start += cd
        i += 1
        cd = pow(2, i)
        end_b = start
        while end_b <= end:
            end_b += cd
        end = end_b - cd
    else:
        i += 1
        cd = pow(2, i)
        end_b = start
        while end_b <= end:
            end_b += cd
        end = end_b - cd
    key *= key_b


print(start) 