# https://www.acmicpc.net/problem/11721

def main():
    sentence = input()
    for _ in range(int(len(sentence)/10)+1):
        print(sentence[:10])
        sentence = sentence[10:]

if __name__ == "__main__":
    main()