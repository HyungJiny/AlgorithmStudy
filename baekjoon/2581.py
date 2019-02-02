# https://www.acmicpc.net/problem/2581
import sys

def main():
    M = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    numbers = [i for i in range(2, N+1)]
    for number in numbers:
        mul = 1
        while number*mul <= N:
            if number*mul in numbers: continue
            numbers.remove(number*mul)
            mul += 1
    print(numbers)

if __name__ == "__main__":
    main()