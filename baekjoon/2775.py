# https://www.acmicpc.net/problem/2775
import sys

rooms = [[0 for _ in range(15)] for _ in range(15)]

def reset_rooms():
    rooms = [[0 for _ in range(15)] for _ in range(15)]

def number_of_resident(k, n):
    if k==0:
        rooms[k][n] = n
        return rooms[k][n]
    if n==1: 
        rooms[k][n] = 1
        return rooms[k][n]
    if rooms[k-1][n] == 0: prev_room = number_of_resident(k-1, n)
    else: prev_room = rooms[k-1][n]
    if rooms[k][n-1] == 0: underflow_room = number_of_resident(k, n-1)
    else: underflow_room = rooms[k][n-1]
    return prev_room + underflow_room

def main():
    for _ in range(int(sys.stdin.readline())):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        print(number_of_resident(k, n))
        reset_rooms()

if __name__ == "__main__":
    main()