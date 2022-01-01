import functools
import sys

input = sys.stdin.readline


def read():
    return list(map(int, list(input().strip())))


def next_positions(level, x, y, touched):
    moves = [(-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (1, 0), (0, 1)]
    possible_moves = []
    n = len(level)
    m = len(level[0])
    for d_x, d_y in moves:
        n_x, n_y = d_x + x, d_y + y
        if 0 <= n_x < n and 0 <= n_y < m and (n_x, n_y) not in touched and level[n_x][n_y] == 0:
            possible_moves.append((n_x, n_y))
    return possible_moves


def solve(level):
    touched = [(0, 0)]

    @functools.lru_cache(maxsize=None)
    def solve_rec(x, y):
        if x == len(level) - 1 and y == len(level[0]) - 1:
            return True
        result = False
        for n_x, n_y in next_positions(level, x, y, touched):
            touched.append((n_x, n_y))
            result = solve_rec(n_x, n_y)
            if result:
                return result
            touched.pop()
        return result

    print("YES" if solve_rec(0, 0) else "NO")


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        a = read()
        b = read()
        solve([a, b])
