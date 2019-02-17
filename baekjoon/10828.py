# https://www.acmicpc.net/problem/10828
import sys

class Stack():
    def __init__(self):
        self.numbers = []
    
    def push(self, number):
        self.numbers.append(number)
    
    def pop(self):
        if self.is_empty(): print(-1)
        else: print(self.numbers.pop())
    
    def is_empty(self):
        if len(self.numbers) == 0: return 1
        else: return 0

    def size(self):
        print(len(self.numbers))

    def empty(self):
        print(self.is_empty())

    def top(self):
        if self.is_empty(): print(-1)
        else: print(self.numbers[-1])


def main():
    stack = Stack()
    for _ in range(int(sys.stdin.readline())):
        line = sys.stdin.readline().strip().split(' ')
        if line[0] == 'push': stack.push(int(line[1]))
        elif line[0] == 'pop': stack.pop()
        elif line[0] == 'size': stack.size()
        elif line[0] == 'empty': stack.empty()
        elif line[0] == 'top': stack.top()


if __name__ == "__main__":
    main()