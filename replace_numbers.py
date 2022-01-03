import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    queries = []
    for i in range(n):
        queries.append(list(map(int, input().split())))
    res = []
    nrs = [i for i in range(10 ** 6)]
    for i in range(n - 1, -1, -1):
        q = queries[i]
        if q[0] == 1:
            res.append(nrs[q[1]])
        else:
            _, x, y = q
            nrs[x] = nrs[y]

    print(*res[::-1])
