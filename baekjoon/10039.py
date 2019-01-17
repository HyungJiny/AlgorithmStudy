# https://www.acmicpc.net/problem/10039
import sys

def main():
    scores = []
    for _ in range(5):
        score = int(sys.stdin.readline())
        if score < 40: score = 40
        scores.append(score)
    print(int(sum(scores) / len(scores)))

if __name__ == "__main__":
    main()