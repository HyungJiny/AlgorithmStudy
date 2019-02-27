# https://www.acmicpc.net/problem/2504
import sys

def main():
    stack = []
    operators = [0]
    is_VPA = True
    for word in sys.stdin.readline().strip():
        if word=='(': 
            stack.append(')')
            if operators[-1] == '+': operators.append(0)
            operators.append('+')
        elif word=='[': 
            stack.append(']')
            if operators[-1] == '+': operators.append(0)
            operators.append('+')
        elif word==')': 
            if operators[-1] == '+': operators.append(1)
            operators.append('*')
            operators.append(2)
        elif word==']':
            if operators[-1] == '+': operators.append(1)
            operators.append('*')
            operators.append(3)
    while len(operators) > 1:
        print(operators)
        if operators[1] == '+': 
            number = int(operators[0]) + int(operators[2])
            operators = [number] + operators[3:]
        elif operators[1] == '*':
            number = int(operators[0]) * int(operators[2])
            operators = [number] + operators[3:]
    print(operators)


if __name__ == "__main__":
    main()