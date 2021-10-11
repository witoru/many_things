# 상수
a, b = map(str, input().split())
a_rev = list(a)
b_rev = list(b)
a_rev.reverse()
b_rev.reverse()
a_rev = int(''.join(a_rev))
b_rev = int(''.join(b_rev))
if a_rev < b_rev:
    print(b_rev)
else:
    print(a_rev)