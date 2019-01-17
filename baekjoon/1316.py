# https://www.acmicpc.net/problem/1316
import sys

def is_groupword(sentence ,prev_words=[]):
    if len(sentence) == 1: return True
    elif sentence[0] == sentence[1]: return is_groupword(sentence[1:], prev_words)
    elif sentence[1] in prev_words: return False
    prev_words.append(sentence[0])
    return is_groupword(sentence[1:], prev_words)

def main():
    count = 0
    repetation = int(sys.stdin.readline())
    for _ in range(repetation): 
        if is_groupword(sys.stdin.readline().strip(), []): count += 1
    print(count)

if __name__ == "__main__":
    main()