# https://www.acmicpc.net/problem/5397
import sys

def solution(log):
    result = ''
    stack01, stack02 = [], []
    for c in log:
        if c=='<' and len(stack01) > 0: stack02.append(stack01.pop())
        elif c=='>' and len(stack02) > 0: stack01.append(stack02.pop())
        elif c=='-' and len(stack01) > 0: stack01.pop()
        elif c!='>' and c!='<' and c!='-': stack01.append(c)
    
    while stack01:
        stack02.append(stack01.pop())
    
    while stack02:
        result += stack02.pop()
    print(result)

if __name__=="__main__":
    for i in range(int(sys.stdin.readline())):
        solution(sys.stdin.readline().strip())