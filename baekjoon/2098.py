# https://www.acmicpc.net/problem/2098
import sys

INF = sys.maxsize

def main():
    n = int(sys.stdin.readline().strip())
    visited = [False for i in range(n)]
    costs = [[int(i) for i in l.strip().split(' ')] for l in sys.stdin.readlines()]

    min_cost = INF
    for i, cost in enumerate(costs):
        for j, c in enumerate(cost):
            if c != 0 and min_cost > c:
                min_cost = c
                x = i
                y = j
    
    answer = min_cost
    print(min_cost)
    visited[x] = True
    visited[y] = True
    
    while(visited.count(False) > 0):
        min_cost = INF
        for i, c in enumerate(costs[y]):
            if not visited[i] and c != 0 and c < min_cost:
                min_cost = c
                y = i
        visited[y]=True
        answer += min_cost
        print(min_cost)
    
    print(answer)

if __name__ == "__main__":
    main()