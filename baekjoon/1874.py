# https://www.acmicpc.net/problem/1874
import sys

def main():
    stack = []
    goal = [int(number) for number in sys.stdin.readlines()[1:]]
    index = 1
    result = ''

    for i in goal:
        while i >= index: 
            stack.append(index)
            index += 1
            result += '+\n'
        if i == stack[-1]:
            stack.pop()
            result += '-\n'
        elif i < stack[-1]:
            result = 'NO'
            break

    print(result.strip())

if __name__ == "__main__":
    main()