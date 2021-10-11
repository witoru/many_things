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
    if h <= n:
        while h <=n:
            arr.append()

h = 3
test2 = ['1-3-5-7-10-13-16-...', '-2-4-6-8-11-14-17...', '1-3-5-7-9-12-15-1...']
arr = [0, 1, 2]
