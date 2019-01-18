# https://www.acmicpc.net/problem/5622
import sys

def main():
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    alphabets = sys.stdin.readline().strip()
    total_time = len(alphabets) * 3
    for alphabet in alphabets:
        for i in range(len(dial)):
            if alphabet in dial[i]:
                total_time += i
                break
    print(total_time)

if __name__ == "__main__":
    main()