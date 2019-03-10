# https://www.acmicpc.net/problem/9020
import sys

def main():
    max = 10000
    prime_numbers = [i for i in range(2, max+1)]
    index = 0
    while index < len(prime_numbers):
        mul = 2
        while prime_numbers[index]*mul <= max:
            target = prime_numbers[index]*mul
            if target in prime_numbers: 
                prime_numbers.remove(target)
            mul += 1
        index += 1

    for line in sys.stdin.readlines():
        number = int(line)
        if number%2: continue
        for prime_number in prime_numbers:
            if prime_number >= number/2: 
                another_number = number - prime_number
                if another_number in prime_numbers: break
        print(another_number, prime_number)

if __name__ == "__main__":
    main()