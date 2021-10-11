N = int(input())
answer = 0
boo = False
n = 0
for i in range(N):
    for j in reversed(str(i+1)):
        answer += int(j) * (10 ** n) + int(j)
        n += 1
    if answer == N:
        print(i+1)
        boo = True
        break
    print(answer)
    answer = 0
    n = 0

if boo == False:
    print(0)