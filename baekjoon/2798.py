import sys
# 조합으로 푸는 방식

stack = []
results = []

# nCr = n-1Cr-1 + n-1Cr
def combination(numbers, n, r, index):
    if r==0:
        results.append(sum(stack))
        return
    elif n==r:
        for i in range(n): stack.append(numbers[index+i])
        results.append(sum(stack))
        for i in range(n): stack.pop()
        return
    else:
        stack.append(numbers[index])
        combination(numbers, n-1, r-1, index+1)
        stack.pop()
        combination(numbers, n-1, r, index+1)

    
if __name__ == "__main__":
    N, M = [int(n) for n in sys.stdin.readline().strip().split(" ")]
    numbers = [int(number) for number in sys.stdin.readline().strip().split(" ")]
    answer = float('inf')

    combination(numbers, N, 3, 0)
    for result in results:
        if result <= M and abs(M-answer) > abs(M-result):
            answer = result

    print(answer)