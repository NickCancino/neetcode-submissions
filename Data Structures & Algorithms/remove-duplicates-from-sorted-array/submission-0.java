class Solution {
    public int removeDuplicates(int[] nums) {
        int r = 1;
        for (int k = 1; k< nums.length; k++){
            if (nums[k] != nums[r-1]){
                nums[r] = nums[k];
                r++;
            }
        }
        return r;
    }
}