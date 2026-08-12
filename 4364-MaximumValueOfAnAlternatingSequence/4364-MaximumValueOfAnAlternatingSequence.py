# Last updated: 12/08/2026, 12:06:34
class Solution(object):
    def maximumValue(self, n, s, m): 
        if n==1:
            return s

        max_odd_index=n-1 if n%2 ==0 else n-2

        up_steps=(max_odd_index+1)//2
        down_steps=max_odd_index//2

        return s +(up_steps *m )- down_steps
        

        
        