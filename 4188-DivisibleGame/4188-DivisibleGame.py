# Last updated: 12/08/2026, 19:12:25
class Solution(object):
    def divisibleGame(self, nums):

        candidates=set()
        for x in nums:
            for d in range(2,int(x**0.5)+1):
                if x%d==0:
                    candidates.add(d)
                    candidates.add(x//d)

            if x>1:
                candidates.add(x)

        max_diff= -float('inf')
        best_k=2

        for k in sorted(candidates or {2}):
            curr_max=0
            max_so_far=-float('inf')
            for x in nums:
                val=x if x%k==0 else -x
                curr_max=max(val,curr_max+val)
                if curr_max >= max_so_far:
                    max_so_far=curr_max

            if max_so_far>max_diff:
                max_diff=max_so_far
                best_k=k


        return(max_diff * best_k) % (10**9+7)
        