# https://www.acmicpc.net/problem/10871
import sys

def main():
    N_X = sys.stdin.readline().strip().split(' ')
    input_array = sys.stdin.readline().strip().split(' ')
    result = ''
    for element in input_array:
        if int(N_X[1]) > int(element):
            result += element + ' '
    print(result)

if __name__ == "__main__":
    main()
