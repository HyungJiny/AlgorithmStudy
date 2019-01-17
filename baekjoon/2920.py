# https://www.acmicpc.net/problem/2920
import sys

def dajangjo(code):
    if len(code) == 1:
        if code[0] == 8: return 'ascending'
        if code[0] == 1: return 'descending'
    else:
        if abs(code[0] - code[1]) == 1: return dajangjo(code[1:])
        else: return 'mixed'

def main():
    input_code = [int(code) for code in sys.stdin.readline().strip().split(' ')]
    print(dajangjo(input_code))

if __name__ == "__main__":
    main()