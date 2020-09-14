# https://www.acmicpc.net/problem/1920
import sys


def solution(A, L):
    A = set(A.split(' '))
    L = L.split(' ')
    for l in L:
        if l in A:
            print('1')
        else:
            print('0')


if __name__ == '__main__':
    N = sys.stdin.readline().strip()
    A = sys.stdin.readline().strip()
    M = sys.stdin.readline().strip()
    L = sys.stdin.readline().strip()
    solution(A, L)
