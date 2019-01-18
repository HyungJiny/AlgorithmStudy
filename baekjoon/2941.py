# https://www.acmicpc.net/problem/2941
import sys

def main():
    sentence = sys.stdin.readline().strip()
    word_count = 0
    i = 0
    while i < len(sentence):
        if len(sentence)-i >= 2 and sentence[i] == 'c':
            if sentence[i+1] == '=' or sentence[i+1] == '-':
                i += 1
        elif sentence[i] == 'd':
            if len(sentence)-i >= 2 and sentence[i+1] == '-':
                i += 1
            elif len(sentence)-i >= 3 and sentence[i+1] == 'z' and sentence[i+2] == '=':
                i += 2
        elif len(sentence)-i >= 2 and ((sentence[i] == 'l' and sentence[i+1] == 'j') \
            or (sentence[i] == 'n' and sentence[i+1] == 'j') \
            or (sentence[i] == 's' and sentence[i+1] == '=') \
            or (sentence[i] == 'z' and sentence[i+1] == '=')):
                i += 1
        word_count += 1
        i += 1
    print(word_count)

if __name__ == "__main__":
    main()