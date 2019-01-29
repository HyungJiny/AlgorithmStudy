# https://www.acmicpc.net/problem/2751
import sys

def main():
    numbers = []
    for _ in range(int(sys.stdin.readline())):
        numbers.append(int(sys.stdin.readline()))
    numbers = sorted(list(set(numbers)))
    for i in numbers: print(i)

if __name__ == "__main__":
    main()