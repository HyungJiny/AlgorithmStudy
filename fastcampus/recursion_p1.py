import sys

def func(n):
    if n <= 1:
       return n
    print(n)
    if (n%2) == 0:
        return func(n/2)
    else:
        return func(3*n+1)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(func(n))