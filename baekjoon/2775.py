# https://www.acmicpc.net/problem/2775
import sys

def number_of_resident(k, n):
    if k==0: return n
    elif n==1: return 1
    return number_of_resident(k-1, n) + number_of_resident(k, n-1)

def main():
    for _ in range(int(sys.stdin.readline())):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        print(number_of_resident(k, n))

if __name__ == "__main__":
    main()