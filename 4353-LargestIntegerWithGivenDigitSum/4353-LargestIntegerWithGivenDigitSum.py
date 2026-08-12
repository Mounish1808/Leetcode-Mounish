# Last updated: 12/08/2026, 19:12:00
class Solution(object):
    def largestInteger(self, n, s):
        if s>9*n:
           return -1

        res="9" * (s // 9) + (str(s % 9) if s % 9 else "")
        return int(res.ljust(n,"0"))
            