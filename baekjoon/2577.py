# https://www.acmicpc.net/problem/2577
import sys

def main():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    C = int(sys.stdin.readline())
    number = str(A * B * C)
    number_counts = [0 for _ in range(10)] 
    for num in number:
        number_counts[int(num)] += 1 
    for count in number_counts:
        print(count)

if __name__ == "__main__":
    main()