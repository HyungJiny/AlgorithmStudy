# https://www.acmicpc.net/problem/10989
# 주어지는 메모리와 시간이 적으니 최대한 활용할 수 있어야함
import sys

def main():
    numbers = [0]*10001
    for _ in range(int(sys.stdin.readline())):
        numbers[int(sys.stdin.readline())] += 1
    for i in range(len(numbers)):
        for _ in range(numbers[i]):
            print(i)
    
if __name__ == "__main__":
    main()