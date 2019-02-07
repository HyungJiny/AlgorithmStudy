# https://www.acmicpc.net/problem/1181
import sys

def get_ascii(word):
    result = ''
    for i in range(len(word)): result += str('%02d'%(ord(word[i])-96))
    return int(result)

def main():
    words = []
    for _ in range(int(sys.stdin.readline())):
        words.append(sys.stdin.readline().strip())
    words = list(set(words))
    for word in sorted(words, key=lambda word: get_ascii(word)): 
        print(word)

if __name__ == "__main__":
    main()