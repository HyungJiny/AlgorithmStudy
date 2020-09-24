# https://www.acmicpc.net/problem/1302
import sys

books = [book.strip() for book in sys.stdin.readlines()[1:]]
book_count = {}
for book in books:
    if book not in book_count:
        book_count[book] = 0
    book_count[book] += 1
print(sorted(book_count.items(), key=lambda x: (-1*x[1], x[0]))[0][0])
