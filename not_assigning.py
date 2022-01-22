# https://codeforces.com/problemset/problem/1627/C

import sys
from collections import defaultdict

input = sys.stdin.readline


def read_int_list():
    return list(map(int, input().split()))


def solve(edges):
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    for neighbours in tree.values():
        if len(neighbours) > 2:
            print(-1)
            return

    # DFS
    res = {}
    touched = set()
    touched.add(1)
    stack = [1]
    parent_prim = {1: 2}

    while stack:
        node = stack.pop()
        prim = parent_prim[node]
        for next_node in tree[node]:
            if next_node not in touched:
                touched.add(next_node)
                stack.append(next_node)
                prim = 3 if prim == 2 else 2
                parent_prim[next_node] = prim
                res[(node, next_node)] = prim

    for a, b in edges:
        if (a, b) in res:
            e = res[(a, b)]
        else:
            e = res[(b, a)]
        print(f'{e} ', end='')
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        edges = []
        for _ in range(n - 1):
            edges.append(read_int_list())
        solve(edges)