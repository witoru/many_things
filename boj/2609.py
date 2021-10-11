def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return abs(a)




a, b = map(int, input().split())

gc = gcd(a, b)
lcm = a*b/gc
print(gc)
print(int(lcm))