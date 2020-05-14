import sys

def func(data):
    if data <= 2:
        return data
    elif data == 3:
        return 4
    return func(data-1) + func(data-2) + func(data-3)
    

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(func(n))