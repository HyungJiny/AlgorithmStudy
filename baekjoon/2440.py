# https://www.acmicpc.net/problem/2440

def main():
    number = int(input())
    for i in range(number, 0, -1):
        star = ""
        for _ in range(i):
            star += "*"
        print(star)

if __name__ == "__main__":
    main()