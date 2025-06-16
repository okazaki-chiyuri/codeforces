import sys

def solve(k, a, b, x, y):
    res = 0
    if x > y:
        a, b = b, a
        x, y = y, x
    if k >= a:
        # Cook as many type 1 shashliks as possible
        res += (k - a) // x + 1
        k -= ((k - a )// x + 1) * x
    if k >= b:
        # Cook as many type 2 shashliks as possible
        res += (k - b) // y + 1
    return res

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    k, a, b, x, y = map(int, input().strip().split())
    print(solve(k, a, b, x, y))
