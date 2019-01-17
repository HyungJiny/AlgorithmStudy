# https://www.acmicpc.net/problem/8958
import sys

def get_score(ox):
    score = 0
    count = 0
    for c in ox:
        if c == 'O': count += 1
        else: count = 0
        score += count
    return score

def main():
    repeatation = int(sys.stdin.readline())
    for _ in range(repeatation):
        print(get_score(sys.stdin.readline().strip()))

if __name__ == "__main__":
    main()