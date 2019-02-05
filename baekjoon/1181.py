# https://www.acmicpc.net/problem/1181
import sys

def main():
    words = []
    for _ in range(int(sys.stdin.readline())):
        words.append(sys.stdin.readline().strip())
    print(words)

if __name__ == "__main__":
    main()