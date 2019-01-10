# https://www.acmicpc.net/problem/4344
import sys

def main():
    repeatation = int(sys.stdin.readline())
    for _ in range(repeatation):
        scores = [int(score) for score in sys.stdin.readline().strip().split(' ')]
        average = sum(scores[1:]) / scores[0]
        count = 0
        for score in scores[1:]: 
            if score > average: count += 1
        print('{:0.3f}%'.format(round((count / scores[0])*100, 3)))

if __name__ == "__main__":
    main()