# https://codeforces.com/contest/1630/problem/C

import sys
from collections import defaultdict

input = sys.stdin.readline
MAX = sys.maxsize

sys.setrecursionlimit(10 ** 9)


# Input functions
def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def read_list():
    s = input()
    return list(s[:len(s) - 1])


def read_int_map():
    return map(int, input().split())


# Solution
class Segment:
    def __init__(self, start, end, cnt):
        self.start = start
        self.end = end
        self.cnt = cnt

    def __repr__(self):
        return f'({self.start} {self.end} {self.cnt})'


def solve(colors):
    idx_map = defaultdict(list)
    for idx, color in enumerate(colors):
        idx_map[color].append(idx)

    segments = []
    for key, value in idx_map.items():
        if len(value) >= 2:
            segments.append((value[0], value[-1]))

    segments.sort()

    if len(segments) <= 0:
        return 0

    i = 1
    ans = []
    curr_seg = Segment(segments[0][0], segments[0][1], 0)
    while i < len(segments):
        if curr_seg.end < segments[i][0]:
            ans.append(curr_seg)
            curr_seg = Segment(segments[i][0], segments[i][1], 0)
        else:
            end = segments[i][1]
            j = i
            while j < len(segments) and segments[j][0] <= curr_seg.end:
                end = max(end, segments[j][1])
                j += 1
            if end > curr_seg.end:
                curr_seg.end = end
                curr_seg.cnt += 1
            i = j
    ans.append(curr_seg)

    res = 0
    for seg in ans:
        res += (seg.end - seg.start - seg.cnt - 1)
    return res


if __name__ == "__main__":
    inp()
    c = read_int_list()
    print(solve(c))
