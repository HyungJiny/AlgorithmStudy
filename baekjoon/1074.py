# https://www.acmicpc.net/problem/1074
import sys


def solution(n, r, c):
    global result
    if n == 2:
        if r == R and c == C:
            print(result)
            return
        result += 1
        if r == R and c+1 == C:
            print(result)
            return
        result += 1
        if r+1 == R and c == C:
            print(result)
            return
        result += 1
        if r+1 == R and c+1 == C:
            print(result)
            return
        result += 1
        return
    solution(n/2, r, c)
    solution(n/2, r, c+n/2)
    solution(n/2, r+n/2, c)
    solution(n/2, r+n/2, c+n/2)


result = 0
N, R, C = map(int, sys.stdin.readline().split(' '))
solution(2**N, 0, 0)
