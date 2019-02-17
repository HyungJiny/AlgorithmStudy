# https://www.acmicpc.net/problem/2108
import sys

def main():
    numbers = [int(number) for number in sys.stdin.readlines()[1:]]
    numbers = sorted(numbers)

    print(round(sum(numbers)/len(numbers))) # 산술평균
    print(numbers[int(len(numbers)/2)]) # 중앙값
    # 최빈값
    number_count = {}
    for number in set(numbers): number_count[number] = 0
    for number in numbers: number_count[number] += 1
    max_values = []
    max_count = max(number_count.values())
    for key in number_count.keys():
        if number_count[key] == max_count:
            max_values.append(key)
    if len(max_values) > 1: print(sorted(max_values)[1])
    else: print(max_values[0])
    print(numbers[-1] - numbers[0]) # 범위


if __name__ == "__main__":
    main()