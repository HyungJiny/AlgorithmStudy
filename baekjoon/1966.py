# https://www.acmicpc.net/problem/1966
import sys


def solution(n, m, docs):
    result = 0
    queue = [(doc, i) for i, doc in enumerate(docs)]
    while len(queue) > 0:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            result += 1
            printed_doc = queue.pop(0)
            if printed_doc[1] == m: break
        else:
            queue.append(queue.pop(0))
        
    return result


if __name__=='__main__':
    for i in range(int(sys.stdin.readline())):
        N, M = list(map(int, sys.stdin.readline().split(' ')))
        print(solution(N, M, list(map(int, sys.stdin.readline().split(' ')))))