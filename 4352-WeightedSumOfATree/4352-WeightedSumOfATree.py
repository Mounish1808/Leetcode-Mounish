# Last updated: 12/08/2026, 19:12:03
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n=len(parent)
        depths=[0]*n

        for i in range(n):
            if depths[i]==0:
                path=[]
                curr=i
                while curr != -1 and depths[curr]==0:
                    path.append(curr)
                    curr=parent[curr]

                d=1 if curr == -1 else depths[curr]+1

                for node in reversed(path):
                    depths[node]=d
                    d += 1

        h=max(depths)
        return sum(val *(h-d+1)for val,d in zip(nums,depths))
        
        