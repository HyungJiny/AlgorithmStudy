# https://www.acmicpc.net/problem/1193
import sys

def main():
    X = int(sys.stdin.readline())
    elements = 1
    line_number = 1
    while elements < X: 
        line_number += 1
        elements += line_number

    elements -= X
    if line_number%2 == 1: 
        denominator = line_number - elements
        numerator = 1 + elements
    else: 
        numerator = line_number - elements
        denominator = 1 + elements    
    print('{}/{}'.format(numerator, denominator))

if __name__ == "__main__":
    main()