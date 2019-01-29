# https://www.acmicpc.net/problem/2750
import sys

def main():
    numbers = []
    for _ in range(int(sys.stdin.readline())):
        numbers.append(int(sys.stdin.readline()))
    for i in sorted(numbers): print(i)   

if __name__ == "__main__":
    main()