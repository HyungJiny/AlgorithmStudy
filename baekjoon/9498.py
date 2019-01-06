# https://www.acmicpc.net/problem/9498
import sys

def main():
    grade = int(sys.stdin.readline().rstrip())
    if grade >= 90: print("A")
    elif grade >= 80 and grade <= 89: print("B")
    elif grade >= 70 and grade <= 79: print("C")
    elif grade >= 60 and grade <= 69: print("D")
    else: print("F")

if __name__ == "__main__":
    main()