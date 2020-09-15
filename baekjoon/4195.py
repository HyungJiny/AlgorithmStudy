# https://www.acmicpc.net/problem/4195
import sys


class networkCalculator():
    def __init__(self):
        self.parents = {}
        self.numbers = {}

    def find(self, x):
        if x == self.parents[x]:
            return x
        else:
            p = self.find(self.parents[x])
            self.parents[x] = p
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.parents[y] = x
            self.numbers[x] += self.numbers[y]


def solution(friends):
    network_calculator = networkCalculator()
    for friend in friends:
        x, y = friend.split(' ')
        if x not in network_calculator.parents:
            network_calculator.parents[x] = x
            network_calculator.numbers[x] = 1
        if y not in network_calculator.parents:
            network_calculator.parents[y] = y
            network_calculator.numbers[y] = 1
        network_calculator.union(x, y)
        print(network_calculator.numbers[network_calculator.find(x)])


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        friends = []
        for i in range(int(sys.stdin.readline())):
            friends.append(sys.stdin.readline().strip())
        solution(friends)
