// Last updated: 12/08/2026, 12:06:44
class Solution {
    public boolean canReach(int[] start, int[] target) {
        return ((start[0]+start[1]&1))==((target[0]+target[1]&1));
        
    }
}