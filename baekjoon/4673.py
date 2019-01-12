# https://www.acmicpc.net/problem/4673

def d(n):
    result = n
    for number in str(n): result += int(number) 
    return result

def main():
    limit = 10000
    is_not_self_number = []
    for i in range(limit):
        is_not_self_number.append(d(i))
    for i in range(limit):
        if not i in is_not_self_number: print(i)

if __name__ == "__main__":
    main()