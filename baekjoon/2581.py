# https://www.acmicpc.net/problem/2581
import sys

def main():
    M = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    numbers = [i for i in range(2, N+1)]
    index = 0
    # 소수 구하기
    while index < len(numbers):
        mul = 2
        number = numbers[index]
        while number*mul <= N:
            mul += 1
            if not number*(mul-1) in numbers: continue
            else: numbers.remove(number*(mul-1))
        index += 1
    numbers = [number for number in numbers if number >= M]
    
    # 결과 출력
    if len(numbers) == 0: print(-1)
    else:
        print(sum(numbers))
        print(numbers[0])

if __name__ == "__main__":
    main()