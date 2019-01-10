# https://www.acmicpc.net/problem/1546
import sys

def main():
    input_number = int(sys.stdin.readline().strip())
    scores = [int(number) for number in sys.stdin.readline().strip().split(' ')]
    max_score = max(scores)
    scores = [score/max_score*100 for score in scores]
    print(sum(scores) / input_number)

if __name__ == "__main__":
    main()