# https://www.acmicpc.net/problem/2110
import sys

n, c = list(map(int, sys.stdin.readline().split(' ')))
homes = sorted([int(line) for line in sys.stdin.readlines()])

start = homes[1] - homes[0]
end = homes[-1] - homes[0]
result = 0

while(start <= end):
    mid = (start+end)//2
    value = homes[0]
    count = 1
    for i in range(1, len(homes)):
        if homes[i] >= value+mid:
            value = homes[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
