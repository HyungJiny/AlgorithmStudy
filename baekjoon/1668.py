# https://www.acmicpc.net/problem/1668
import sys

n = int(sys.stdin.readline())
trophies = [int(line) for line in sys.stdin.readlines()]

left_count = 1
max_trophy = trophies[0]
for i in range(n):
    if max_trophy < trophies[i]:
        left_count += 1
        max_trophy = trophies[i]

right_count = 1
max_trophy = trophies[-1]
for i in range(n-1, -1, -1):
    if max_trophy < trophies[i]:
        right_count += 1
        max_trophy = trophies[i]

print('{}\n{}'.format(left_count, right_count))
