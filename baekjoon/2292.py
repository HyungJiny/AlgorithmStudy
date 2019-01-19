# https://www.acmicpc.net/problem/2292
import sys

def main():
    input_room = int(sys.stdin.readline())
    room_line = 1
    min_room_in_line = 1
    while min_room_in_line < input_room:
        min_room_in_line += 6*room_line
        room_line += 1
    print(room_line)

if __name__ == "__main__":
    main()