# https://www.acmicpc.net/problem/2908
import sys

def reverse(number):
    result = ''
    for i in range(len(number)-1, -1, -1): result += number[i]
    return int(result)

def main():
    numbers = sys.stdin.readline().strip().split(' ')
    A = reverse(numbers[0])
    B = reverse(numbers[1])
    if A > B: print(A)
    else: print(B)

if __name__ == "__main__":
    main()