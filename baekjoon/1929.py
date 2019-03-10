# https://www.acmicpc.net/problem/1929
import sys

def main():
    M, N = (int(number) for number in sys.stdin.readline().strip().split(' '))
    numbers = [1 for _ in range(N+1)]
    numbers[0] = numbers[1] = 0
    for i in range(2, N+1):
        mul = 2
        while i*mul <= N:
            numbers[i*mul] = 0
            mul += 1

    for i in range(M, N+1):
        if numbers[i]: 
            print(i)

if __name__ == "__main__":
    main()