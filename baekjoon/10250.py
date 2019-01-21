# https://www.acmicpc.net/problem/10250
import sys

def main():
    for _ in range(int(sys.stdin.readline())):
        H, W, N = (int(number) for number in sys.stdin.readline().strip().split(' '))
        flow = N % H
        room = 1 + int(N/H)
        if flow == 0: 
            flow = H
            room -= 1
        print('{}{:02}'.format(flow, room))

if __name__ == "__main__":
    main()