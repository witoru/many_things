K = int(input())
stack = []
s = 0
for _ in range(K):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()

for i in stack:
    s += i
print(s)