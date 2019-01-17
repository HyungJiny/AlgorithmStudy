# https://www.acmicpc.net/problem/1157
import sys

def main():
    alphabets = sys.stdin.readline().strip().upper()
    alphabet_count = {alphabet : 0 for alphabet in set(alphabets)}
    for alphabet in alphabets: alphabet_count[alphabet] += 1
    value_list = sorted(list(alphabet_count.values()), reverse=True)
    max_value = value_list[0]
    if len(value_list) > 1 and value_list[0] == value_list[1]: print('?')
    else: 
        for alphabet in alphabet_count.keys(): 
            if alphabet_count[alphabet] == max_value: 
                print(alphabet)
                break

if __name__ == "__main__":
    main()