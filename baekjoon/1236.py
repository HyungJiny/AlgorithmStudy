# https://www.acmicpc.net/problem/1236
import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))
castle = [line.strip() for line in sys.stdin.readlines()]

row_count = 0
column_count = 0

column_X = []

for i in range(n):
    if 'X' not in castle[i]:
        row_count += 1
    for j in range(m):
        if castle[i][j] == 'X':
            column_X.append(j)

for j in range(m):
    if j not in column_X:
        column_count += 1


print(max(row_count, column_count))
