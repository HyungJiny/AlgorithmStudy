# https://www.acmicpc.net/problem/1110
import sys

def main():
    first_number = sys.stdin.readline().strip()
    if int(first_number) < 10: first_number = '0'+first_number
    cycle = 0
    temp = first_number
    while True:
        temp = temp[1] + str(int(temp[0]) + int(temp[1]))[-1]
        cycle += 1
        if temp == first_number: break
    print(cycle)

if __name__ == "__main__":
    main()