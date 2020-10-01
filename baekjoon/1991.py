# https://www.acmicpc.net/problem/1991
import sys

bi_tree = {} 
result = ''

def preorder(node):
    global result
    if node == '.':
        return
    result += node
    preorder(bi_tree[node]['left'])
    preorder(bi_tree[node]['right'])

def inorder(node):
    global result
    if node == '.':
        return
    inorder(bi_tree[node]['left'])
    result += node
    inorder(bi_tree[node]['right'])

def postorder(node):
    global result
    if node == '.':
        return
    postorder(bi_tree[node]['left'])
    postorder(bi_tree[node]['right'])
    result += node
    
    
if __name__=='__main__':
    n = int(sys.stdin.readline())
    head = ''
    for i in range(n):
        name, left, right = map(str, sys.stdin.readline().strip().split())
        if i == 0: head = name
        bi_tree[name] = {'left': left, 'right': right}
    
    preorder(head)
    print(result)
    result = ''
    inorder(head)
    print(result)
    result = ''
    postorder(head)
    print(result)
