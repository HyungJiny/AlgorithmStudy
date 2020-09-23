# https://www.acmicpc.net/problem/1568
import sys

n = int(sys.stdin.readline())
k = 1
count = 0
while n > 0:
    n -= k
    k += 1
    if n < k:
        k = 1
    count += 1
print(count)
