# The roof is a rectangle of size w×h
#  with the bottom left corner at the point (0,0)
#  on the plane. Your team needs to completely cover this roof with identical roofing sheets of size 𝑎×𝑏
# , with the following conditions:

# The sheets cannot be rotated (not even by 90∘
# ).
# The sheets must not overlap (but they can touch at the edges).
# The sheets can extend beyond the boundaries of the rectangular roof.
# A novice from your team has already placed two such sheets on the roof in such a way that the sheets do not overlap and each of them partially covers the roof.

# Your task is to determine whether it is possible to completely tile the roof without removing either of the two already placed sheets.

import sys
input = sys.stdin.readline

def solve(w, h, a, b, x1, y1, x2, y2):
    # check if 