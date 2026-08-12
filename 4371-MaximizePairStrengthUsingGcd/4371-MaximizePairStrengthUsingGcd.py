# Last updated: 12/08/2026, 12:06:36
class Solution(object):
    def maxPairStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_gcd(x,y):
            while y:
                x,y=y,x%y
            return x
        max_strength=0
        n=len(nums)

        for i in range(n):
            for j in range(i+1,n):
                a,b=nums[i],nums[j]
                g=get_gcd(a,b)

                strength = (a*b)//(g*g)

                if strength > max_strength:
                    max_strength=strength
        return max_strength