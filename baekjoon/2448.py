# https://www.acmicpc.net/problem/2448
import sys

def upgrade_triangle(basic):
    result = []
    space = ''
    for _ in range(int(len(basic[0])/2)+1): space += ' '
    for line in basic: result.append(space+line+space)
    for line in basic: result.append(line+' '+line)
    return result

def main():
    # n = 3*2**k (k <= 10)
    n = int(sys.stdin.readline())/3
    k = 0
    triangle = ['  *  ', ' * * ', '*****']
    while n > 1:
        k += 1
        n = n/2
    for _ in range(k): triangle = upgrade_triangle(triangle)
    for line in triangle: print(line)

if __name__ == "__main__":
    main()