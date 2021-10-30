a, b, v = map(int, input().split())
if v - a - 1 < 0:
    print(1)
else:
    print(((v - a - 1) // (a - b)) + 2)