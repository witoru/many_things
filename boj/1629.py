def asdf(a, b):
    global c
    if b == 1:
        return a%c
    tmp = asdf(a, int(b/2))
    if b%2 == 1:
        return (a%c * tmp%c * tmp%c) % c
    else :
        return (tmp%c * tmp%c)%c

a, b, c = map(int, input().split())

print(asdf(a, b))