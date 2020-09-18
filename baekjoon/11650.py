# https://www.acmicpc.net/problem/11650
import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    points = []
    for i in range(n):
        point = sys.stdin.readline().strip().split(' ')
        points.append((int(point[0]), int(point[1])))
    for point in sorted(points, key=lambda x: (x[0], x[1])):
        print('{} {}'.format(point[0], point[1]))
