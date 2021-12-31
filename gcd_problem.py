import sys
from math import gcd

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    for i in range(0, n):
        m = int(input())
        if m % 2 == 0:
            print(f"{m - 3} 2 1")
        else:
            j = m - 4
            k = 3
            while True:
                if gcd(j, k) == 1:
                    print(f"{j} {k} 1")
                    break
                else:
                    j -= 2
                    k += 2
