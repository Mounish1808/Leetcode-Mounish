// Last updated: 12/08/2026, 12:06:48
class Solution{
    int count =0;
    public int
    countDominantNodes(TreeNode root){
        TreeNode I=root;
        dfs(I);
        return count;
    }
        private int dfs(TreeNode node){
            if(node==null)return Integer.MIN_VALUE;
            int left=dfs(node.left);
            int right=dfs(node.right);
            int max=Math.max(node.val,Math.max(left,right));
            if(node.val==max){
                count++;
            }
            return max;
        }
}