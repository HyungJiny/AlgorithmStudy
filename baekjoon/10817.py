# https://www.acmicpc.net/problem/10817
import sys

def main():
    numbers = sys.stdin.readline().rstrip().split(' ')
    numbers = [int(number) for number in numbers]
    print(sorted(numbers)[1])
    
if __name__ == "__main__":
    main()