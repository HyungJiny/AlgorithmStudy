# https://www.acmicpc.net/problem/1181
import sys

def main():
    words = []
    for _ in range(int(sys.stdin.readline())):
        words.append(sys.stdin.readline().strip())
    words = list(set(words))
    print(sorted(words, key=lambda word: len(word)))

if __name__ == "__main__":
    main()