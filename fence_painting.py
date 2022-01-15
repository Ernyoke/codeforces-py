# https://codeforces.com/contest/1481/problem/C

import sys
from collections import defaultdict

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def solve(initial, desired, painters):
    needs_paint = defaultdict(list)
    wants_paint = defaultdict(list)
    for index, (init, des) in enumerate(zip(initial, desired)):
        if init != des:
            needs_paint[des].append(index + 1)
        wants_paint[des].append(index + 1)
    last_painter = painters.pop()
    if last_painter not in wants_paint:
        print("NO")
        return
    last_to_paint = wants_paint[last_painter][0]
    if last_painter in needs_paint:
        last_to_paint = needs_paint[last_painter].pop()
        if len(needs_paint[last_painter]) <= 0:
            del needs_paint[last_painter]
    res = []
    for p in painters:
        if p in needs_paint:
            res.append(needs_paint[p].pop())
            if len(needs_paint[p]) <= 0:
                del needs_paint[p]
        elif p in wants_paint:
            res.append(wants_paint[p][0])
        else:
            res.append(last_to_paint)
    res.append(last_to_paint)
    if len(needs_paint.keys()) > 0:
        print("NO")
        return
    print("YES")
    print(*res)


if __name__ == "__main__":
    for _ in range(int(input())):
        _, _ = read()
        initial = read()
        desired = read()
        painters = read()
        solve(initial, desired, painters)