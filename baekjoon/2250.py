# https://www.acmicpc.net/problem/2250
import sys

tree = {}
n = int(sys.stdin.readline())
head = 0
for i in range(n):
    data, left, right = map(int, sys.stdin.readline().split(' '))
    if i == 0: head = data
    tree[data] = {'left': left, 'right': right}

ordered_data = []
def inorder(start, level):
    if start == -1:
        return
    inorder(tree[start]['left'], level+1)
    ordered_data.append((start, level-1))
    inorder(tree[start]['right'], level+1)

inorder(head, 1)

level_datas = {}
for i, data in enumerate(ordered_data):
    if data[1] not in level_datas:
        level_datas[data[1]] = []
    level_datas[data[1]].append(i)

level_distance = []
for key, item in level_datas.items():
    level_distance.append((key+1, max(item) - min(item) + 1))
max_distance = sorted(level_distance, key=lambda x: (x[1], -x[0]))[-1]
print('{} {}'.format(max_distance[0], max_distance[-1]))
