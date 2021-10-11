a, d, k = map(int, input().split())
d = d/100
k = k/100
sum = 0
per = []
rev = 1
count = 1

while d != 1:
    for i in per:
        rev *= (1-i)
    sum += a * count * d * rev
    per.append(d)
    d = d * (1 + k)
    if d > 1:
        d = 1
    count += 1
    rev = 1

for i in per:
    rev *= (1-i)
sum += a * count * d * rev

print(sum)