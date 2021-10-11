arr = []
arr.append(input())
i = 0
while arr[i] != '0':
    arr.append(input())
    i += 1
arr.remove('0')

for str in arr:
    n = len(str)
    if n % 2 == 1:
        if str[:(n//2)] == ''.join(reversed(str[(n//2)+1:])):
            print("yes")
        else:
            print("no")
    else:
        if str[:(n//2)] == ''.join(reversed(str[(n//2):])):
            print("yes")
        else:
            print("no")
