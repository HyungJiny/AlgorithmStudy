# https://www.acmicpc.net/problem/2739

def main():
    number = int(input())
    for i in range(1, 10):
        print(number, "*", i, "=", number*i)

if __name__ == "__main__":
    main()