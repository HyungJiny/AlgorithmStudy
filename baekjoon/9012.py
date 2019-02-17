# https://www.acmicpc.net/problem/9012
import sys

def main():
    for _ in range(int(sys.stdin.readline())):
        stack = []
        result = 'YES'
        line = sys.stdin.readline().strip()
        for word in line:
            if word=='(': stack.append(')')
            elif word==')' and len(stack) > 0: stack.pop()
            elif word==')' and len(stack) < 1: result = 'NO'
        if len(stack) > 0: result = 'NO'
        print(result)

if __name__ == "__main__":
    main()