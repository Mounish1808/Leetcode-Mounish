# Last updated: 12/08/2026, 19:12:17
class Solution(object):
    def aggregateTimeSeries(self, series1, series2):
        dict1 = dict(series1)
        dict2 = dict(series2)

        timestamps = sorted(list(set(dict1.keys()) | set(dict2.keys())))

        res = []
        next_val1 = 0
        next_val2 = 0

        for t in reversed(timestamps):
            if t in dict1:
                val1 = dict1[t]
                next_val1=val1
            else:
                val1 = next_val1

            if t in dict2:
                val2 = dict2[t]
                next_val2 = val2
            else:
                val2 = next_val2

            res.append([t,val1 + val2])

        return res[::-1]

                
        