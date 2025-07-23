
# # https://codeforces.com/problemset/problem/2065/G

# import sys
# from collections import Counter
# input = sys.stdin.readline

# N = 200000
# factor = [0] * (N + 1)
# primes = []
# semi_primes = set()
# for i in range(2, N + 1):
#     if factor[i] == 0:
#         primes.append(i)
#         factor[i] = i
#     for p in primes:
#         if i * p > N:
#             break
#         if factor[i] == i:
#             semi_primes.add(i * p)
#         factor[i * p] = p
#         if factor[i] == p:
#             break

# T = int(input())

# # print(sorted(list(semi_primes)[:10]))

# def solve(lst):
#     cnt = Counter(lst)
#     p = 0
#     res = 0
#     for k in (primes & cnt.keys()):
#         res += cnt[k] * p
#         p += cnt[k]
#     for k in sorted(semi_primes & cnt.keys()):
#         # if k in primes:
#         #     res += p * cnt[k]
#         #     # res += cnt[k] * (cnt[k] - 1) // 2
#         #     p += cnt[k]
#         #     continue
#         f = factor[k]
#         if k // f in primes:
#             res += cnt[k] * (cnt[k] + 1) // 2
#             res += cnt[k] * cnt[f]
#             if k // f != f:
#                 res += cnt[k] * cnt[k // f]
#     return res

# for _ in range(T):
#     n = int(input())
#     lst = list(map(int, input().strip().split()))
#     print(solve(lst))


import sys
input = sys.stdin.readline

# 1) Build spf up to 200000
MAXN = 200000
spf = [0] * (MAXN + 1)
primes = []
for i in range(2, MAXN + 1):
    if spf[i] == 0:
        spf[i] = i
        primes.append(i)
    for p in primes:
        ip = i * p
        if p > spf[i] or ip > MAXN:
            break
        spf[ip] = p

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    cnt = [0] * (m + 1)
    for x in a:
        cnt[x] += 1

    res = 0
    prime_count = 0
    # localize for speed
    spf_loc = spf
    cnt_loc = cnt

    for k in range(2, m + 1):
        ck = cnt_loc[k]
        if ck == 0:
            continue
        fk = spf_loc[k]
        if fk == k:
            # k is prime: pair with all earlier primes
            res += prime_count * ck
            prime_count += ck
        else:
            # check semi-prime: k = p * q
            q = k // fk
            if spf_loc[q] == q:
                # (k,k) pairs
                res += ck * (ck + 1) // 2
                # (p,k) and (q,k) pairs
                res += ck * cnt_loc[fk]
                if q != fk:
                    res += ck * cnt_loc[q]

    print(res)
