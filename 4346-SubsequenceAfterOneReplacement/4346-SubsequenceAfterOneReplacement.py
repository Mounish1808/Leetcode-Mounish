# Last updated: 12/08/2026, 19:12:13
class Solution(object):
    def canMakeSubsequence(self, s, t):
        s,t=s.lower(),t.lower()
        n,m=len(s),len(t)

        L=[m]*(n+1)
        L[0]=-1

        curr = 0

        for i in range(n):
            curr=t.find(s[i],curr)
            if curr==-1: break
            L[i+1]=curr
            curr+=1

        R=[-1]*(n+1)
        R[n]=m

        curr=m-1
        for i in range(n-1,-1,-1):
            curr=t.rfind(s[i],0,curr+1)
            if curr == -1:break
            R[i]=curr
            curr -=1

        return any(L[i] + 1< R[i+1] for i in range(n))
        