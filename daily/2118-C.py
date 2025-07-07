import sys
import heapq
input = sys.stdin.readline
# https://codeforces.com/problemset/problem/2118/C

def solve(lst, k):
    res = sum([x.bit_count() for x in lst])
    # get the lowest zero bit of each number => add which to achieve one more one bit
    h = [( ~x & (x + 1), x) for x in lst]
    heapq.heapify(h)
    while k > 0 and h:
        z, x = heapq.heappop(h)
        if z == 0:
            break
        if z > k:
            break
        k -= z
        res += 1
        x |= z
        heapq.heappush(h, ( ~x & (x + 1), x))
    return res

N = int(input())
for _ in range(N):
    n, k = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    print(solve(lst, k))
