# https://www.acmicpc.net/problem/1475
import sys

def main():
    # 가장 많이 나온 숫자에 맞춰 세트를 구매하면 됨
    # 처음부터 중복될 수 있는 9를 6으로 모두 바꾸고 시작하면 편함
    number = sys.stdin.readline().strip().replace('9', '6')
    number_count = [0 for _ in range(9)]
    for n in number: number_count[int(n)] += 1
    number_count[6] = int(number_count[6]/2) + number_count[6]%2
    print(max(number_count))

if __name__ == "__main__":
    main()