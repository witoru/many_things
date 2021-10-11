n = int(input())
arr = []
answer = []
stack = []
a = 0
key = False
for _ in range(n):
    arr.append(int(input()))

for i in range(1, n+1):
    stack.append(i)
    answer.append('+')
    while len(stack) != 0 and stack[len(stack) - 1] == arr[a]:
        stack.pop()
        answer.append('-')
        a += 1
    if len(stack) != 0 and stack[len(stack) - 1] > arr[a]:
        key = True
        break

if key == True:
    print("NO")
else:
    for i in answer:
        print(i)