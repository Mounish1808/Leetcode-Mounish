# Last updated: 12/08/2026, 19:12:10
class Solution(object):
    def minimumCost(self, nums, k):

       

        total_cost=0
        current_resources=k
        operation_count=0
        MOD=10**9+7

        for num in nums:
            if current_resources<num:
                deficit=num-current_resources
                needed_operations=(deficit+k-1)//k


                start_cost=operation_count+1
                end_cost=operation_count+needed_operations

                cost_for_this_step=(start_cost+end_cost)*needed_operations//2

                total_cost+=cost_for_this_step
                operation_count+=needed_operations
                current_resources+=needed_operations*k


            current_resources -=num

        return total_cost%MOD


     

       