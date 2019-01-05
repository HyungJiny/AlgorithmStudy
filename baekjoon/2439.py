# https://www.acmicpc.net/problem/2439

def main():
    number = int(input())
    for i in range(1, number+1):
        star = ""
        for _ in range(i):
            star += "*"
        for _ in range(number-i):
            star = " " + star
        print(star)

if __name__ == "__main__":
    main()