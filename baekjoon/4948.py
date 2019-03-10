# https://www.acmicpc.net/problem/4948
import sys

def main():
    max = 123456
    numbers = [1 for _ in range(max*2+1)]
    numbers[0] = numbers[1] = 0
    
    for i in range(2, max*2+1):
        mul = 2
        while i*mul <= max*2:
            numbers[i*mul] = 0
            mul += 1

    for number in sys.stdin.readlines():
        min = int(number)
        if min == 0: break
        print(sum(numbers[min+1:min*2+1]))

if __name__ == "__main__":
    main()