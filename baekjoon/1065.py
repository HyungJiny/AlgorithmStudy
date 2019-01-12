# https://www.acmicpc.net/problem/1065
import sys

def hansu(number):
    if number < 100: return True
    gap = int(str(number)[0]) - int(str(number)[1])
    for i in range(len(str(number))-1):
        if gap != int(str(number)[i])-int(str(number)[i+1]): return False
    return True

def main():
    n = int(sys.stdin.readline())
    count = 0
    for i in range(1, n+1): 
        if hansu(i): count += 1
    print(count)

if __name__ == "__main__":
    main()