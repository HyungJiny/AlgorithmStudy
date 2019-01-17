# https://www.acmicpc.net/problem/2675
import sys

def main():
    repetation = int(sys.stdin.readline())
    for _ in range(repetation):
        input_line = sys.stdin.readline().strip().split()
        result = ''
        for char in input_line[1]:
            for _ in range(int(input_line[0])): result += char
        print(result)

if __name__ == "__main__":
    main()