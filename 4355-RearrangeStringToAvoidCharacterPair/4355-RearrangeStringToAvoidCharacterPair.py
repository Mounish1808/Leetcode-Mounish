# Last updated: 12/08/2026, 19:12:07
class Solution(object):
    def rearrangeString(self, s, x, y):
        return "".join(sorted(s,key=lambda c: (c == x) - (c==y)))
        
        