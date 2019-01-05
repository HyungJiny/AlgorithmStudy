# https://www.acmicpc.net/problem/15552
import sys

def main():
    # python 입력을 빠르게 받는 방법
    # rstrip()은 '\n'을 없애기 위한 작업
    repeatition = int(sys.stdin.readline().rstrip())
    for _ in range(repeatition):
        numbers = sys.stdin.readline().rstrip().split(" ")
        print(int(numbers[0]) + int(numbers[1]))

if __name__ == "__main__":
    main()