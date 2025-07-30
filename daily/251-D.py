# https://codeforces.com/problemset/problem/251/D
import sys
from functools import reduce
input = sys.stdin.readline

def solve(lst, n):
    s = reduce(lambda x, y: x^y, lst)
    # get \neg s
    m = s.bit_length()
    s = ((1 << m) - 1) ^ s
    selected = [1] * n
    for i in range(m-1, -1, -1):
        bit = (s >> i) & 1
        if bit == 0:
            continue
        for j in range(n):
            if selected[j]==1 and not (lst[j] >> i) & 1:
                selected[j] = 2
    return selected

# T = int(input())
# for _ in range(T):
n = int(input())
lst = list(map(int, input().strip().split()))
selected = solve(lst, n)
print(*selected)
        
