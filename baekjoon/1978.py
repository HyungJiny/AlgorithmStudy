# https://www.acmicpc.net/problem/1978
import sys

def is_prime_number(number):
    if number == 1: return False
    for i in range(number-1, 1, -1):
        if number%i == 0: return False
    return True

def main():
    number_count = int(sys.stdin.readline())
    numbers = [int(num) for num in sys.stdin.readline().strip().split(' ')]
    for number in numbers:
        if not is_prime_number(number):
            number_count -= 1
    print(number_count)

if __name__ == "__main__":
    main()