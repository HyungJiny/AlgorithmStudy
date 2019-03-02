# https://www.acmicpc.net/problem/2504
import sys

def main():
    stack = []
    scores = []
    is_VPS = True
    is_closed = False
    for word in sys.stdin.readline().strip():
        if word == '(' or word == '[': 
            stack.append(word)
            if not is_closed: is_closed = True
            else: scores.append(1)
        elif word == ')':
            if len(stack) == 0 or stack[-1] != '(':
                is_VPS = False
                break
            stack.pop()
            scores.append(scores.pop()*2)
            is_closed = False
        elif word == ']':
            if len(stack) == 0 or stack[-1] != '[':
                is_VPS = False
                break
            stack.pop()
            scores.append(scores.pop()*3)
            is_closed = False
        if len(stack) == 0: scores = [sum(scores)]
        print(scores)

    if is_VPS: print(scores)
    else: print(0)


if __name__ == "__main__":
    main()