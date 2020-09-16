# https://www.acmicpc.net/problem/10814
import sys

if __name__ == '__main__':
    members = []
    for i, line in enumerate(sys.stdin.readlines()[1:]):
        member = line.strip().split(' ')
        members.append((i, int(member[0]), member[1]))

    for member in sorted(members, key=lambda x: (x[1], x[0])):
        print('{} {}'.format(member[1], member[2]))
