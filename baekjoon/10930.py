# https://www.acmicpc.net/problem/BaseException

import sys
import hashlib


def solution(input_text):
    encoded_data = input_text.encode()
    return hashlib.sha256(encoded_data).hexdigest()


if __name__ == "__main__":
    print(solution(sys.stdin.readline().strip()))
