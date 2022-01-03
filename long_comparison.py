import sys

input = sys.stdin.readline


def compare(values):
    for a, a_zeros, b, b_zeros in values:
        x = a
        while x > 1:
            x = x / 10
            a_zeros += 1

        y = b
        while y > 1:
            y = y / 10
            b_zeros += 1

        if a_zeros > b_zeros:
            print('>')
        elif a_zeros < b_zeros:
            print('<')
        else:
            if x > y:
                print('>')
            elif x < y:
                print('<')
            else:
                print('=')


if __name__ == "__main__":
    n = int(input())
    values = []
    for i in range(0, n):
        a, a_zeros = map(int, input().split())
        b, b_zeros = map(int, input().split())
        values.append((a, a_zeros, b, b_zeros))
    compare(values)
