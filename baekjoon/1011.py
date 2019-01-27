# https://www.acmicpc.net/problem/1011
import sys

def operate_count(x, y):
    # 단계의 2배만큼 거리가 대칭을 이루며 커짐을 이용
    distance = y-x
    step = 1
    while distance > step*2:
        distance -= step*2
        step += 1
    if distance > step: return step*2
    else: return step*2-1
        
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        X, Y = (int(number) for number in sys.stdin.readline().strip().split(' '))
        print(operate_count(X, Y))

if __name__ == "__main__":
    main()