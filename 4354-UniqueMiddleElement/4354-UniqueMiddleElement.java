// Last updated: 12/08/2026, 19:11:58
class Solution {
    public boolean isMiddleElementUnique(int[] nums) {
        int n=nums.length;

        int middleElement=nums[n/2];
        int count =0;

        for(int num:nums){
            if(num==middleElement){
                count++;
            }
        }
        return count==1;        
    }
}