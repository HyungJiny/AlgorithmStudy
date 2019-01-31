# https://www.acmicpc.net/problem/1427
import sys

def main():
    number = [int(num) for num in sys.stdin.readline().strip()]
    number = sorted(number, reverse=True)
    result = ''
    for num in number: result += str(num)
    print(result)

if __name__ == "__main__":
    main()