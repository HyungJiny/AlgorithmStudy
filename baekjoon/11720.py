# https://www.acmicpc.net/problem/11720

def main():
    number = int(input())
    num_for_cal = input()
    result = 0
    for i in range(number):
        result += int(num_for_cal[i])    
    print(result)

if __name__ == "__main__":
    main()