# https://www.acmicpc.net/problem/2775
import sys

def number_of_resident(k, n):
    floor = [[0 for _ in range(n)] for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if i==0: floor[i][j] = j+1
            elif j==0: floor[i][j] = 1
            else: floor[i][j] = floor[i-1][j] + floor[i][j-1]
    return floor[k][n-1]

def main():
    for _ in range(int(sys.stdin.readline())):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        print(number_of_resident(k, n))

if __name__ == "__main__":
    main()