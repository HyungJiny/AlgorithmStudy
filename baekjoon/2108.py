# https://www.acmicpc.net/problem/2108
import sys

def main():
    numbers = [int(number) for number in sys.stdin.readlines()[1:]]
    numbers = sorted(numbers)
    print(round(sum(numbers)/len(numbers))) # 산술평균
    print(numbers[int(len(numbers)/2)]) # 중앙값
    
    print(numbers[-1] - numbers[0]) # 범위


if __name__ == "__main__":
    main()