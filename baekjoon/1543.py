import sys

line = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()

print(len(line.split(word))-1)
