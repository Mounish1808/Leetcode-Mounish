// Last updated: 12/08/2026, 19:12:14
class Solution {
    public int maxValidPairSum(int[] nums, int k) {
        int n=nums.length;

        if(n<=k){
            return -1;
        }
        int maxSum=Integer.MIN_VALUE;
        int maxPrefix=Integer.MIN_VALUE;

        for(int j=k;j<n;j++){
            maxPrefix=Math.max(maxPrefix,nums[j-k]);

            maxSum=Math.max(maxSum,maxPrefix+nums[j]);
        }
        return maxSum;
    }
    public static void main(String[]args){
        Solution sol=new Solution();
        int[] nums={1,3,5,2,8};
        int k=2;
        System.out.println("Output: " + sol.maxValidPairSum(nums,k));
    }
}