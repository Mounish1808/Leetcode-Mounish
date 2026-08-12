# Last updated: 12/08/2026, 19:12:22
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n=len(nums)

        valid_count=0

        for i in range(n):
            evens = 0
            odds = 0

            for j in range(i,n):
                if nums[j]%2==0:
                    evens +=1
                else:
                    odds +=1

                if odds>0 and (evens * b <=odds *a):
                    valid_count +=1


        return valid_count
        