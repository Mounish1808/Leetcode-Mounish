# Last updated: 12/08/2026, 19:11:57
class Solution(object):
    def maxDigitRange(self, nums):
        r=lambda x: int(max(str(x)))-int(min(str(x)))
        m=max(map(r,nums))
        return sum(x for x in nums if r(x) == m)
        