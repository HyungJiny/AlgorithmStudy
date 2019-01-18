# https://www.acmicpc.net/problem/10809
import sys

def main():
    sentence = sys.stdin.readline().strip()
    alphabets = [-1 for _ in range(26)]
    index = 0
    for char in sentence:
        if alphabets[ord(char) - 97] == -1: alphabets[ord(char) - 97] = index
        index += 1
    result = ''
    for alphabet in alphabets: result += str(alphabet)+' '
    print(result)

if __name__ == "__main__":
    main()