# https://www.acmicpc.net/problem/6064
import sys

def gcd(a, b):
    # 유클리드 호제법을 이용한 최대공약수
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

def lcm(a, b):
    # 최소공배수
    return a*b//gcd(a, b)

def kaing(M, N, X, Y):
    max_k = lcm(M, N)
    # 최소공배수만큼만 계산
    while X < max_k:
        if X == Y: return X
        if X > Y: Y += N
        elif X < Y: X += M
    # 해당 계산 안에 끝나지 않는다면 없는 것
    return -1
    
def main():
    for _ in range(int(sys.stdin.readline())):
        M, N, X, Y = (int(number) for number in sys.stdin.readline().strip().split(' '))
        print(kaing(M, N, X, Y))

if __name__ == "__main__":
    main()