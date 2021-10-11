# https://www.acmicpc.net/problem/10951
import sys

arr = sys.stdin.readlines()
for i in arr:
    a, b = map(int, i.split())
    print(a+b)