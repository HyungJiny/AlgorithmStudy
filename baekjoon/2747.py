# https://www.acmicpc.net/submit/2747
import sys

fibo_result = {0: 0, 1: 1}


def fibo(n):
    if n not in fibo_result:
        fibo_result[n] = fibo(n-1) + fibo(n-2)
    return fibo_result[n]


print(fibo(int(sys.stdin.readline())))
