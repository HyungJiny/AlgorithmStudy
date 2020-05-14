import sys

def isPalindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return isPalindrome(word[1:-1])

def main():
    word = sys.stdin.readline().strip()
    print(isPalindrome(word))

if __name__ == "__main__":
    main()