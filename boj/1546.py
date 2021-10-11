N = int(input())
sub = list(map(int, input().split()))
M = 0
avg = 0
for i in sub:
    if M < i:
        M = i
for i in range(len(sub)):
    sub[i] = sub[i]/M*100
for i in sub:
    avg += i
print(avg/N)