# Last updated: 12/08/2026, 12:06:50
class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):

        h1,m1,s1=map(int,startTime.split(':'))
        start_secs=h1*3600+m1*60+s1

        h2,m2,s2=map(int,endTime.split(':'))
        end_secs=h2*3600+m2*60+s2

        return end_secs-start_secs
       
        