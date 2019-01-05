# https://www.acmicpc.net/problem/2441

def main():
    number = int(input())
    for i in range(number, 0, -1):
        star = ""
        for _ in range(i):
            star += "*"
        for _ in range(number-i):
            star = " " + star
        print(star)

if __name__ == "__main__":
    main()