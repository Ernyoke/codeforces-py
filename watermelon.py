import sys

input = sys.stdin.readline

if __name__ == "__main__":
    val = int(input())
    print("YES" if val > 2 and val % 2 == 0 else "NO")
