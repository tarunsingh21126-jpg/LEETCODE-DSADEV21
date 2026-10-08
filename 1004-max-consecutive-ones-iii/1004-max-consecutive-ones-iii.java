class Solution {
    public int longestOnes(int[] nums, int k) {

        int left = 0;
        int zeroCount = 0;
        int maxLength = 0;

        for (int right = 0; right < nums.length; right++) {

            // Include nums[right]
            if (nums[right] == 0) {
                zeroCount++;
            }

            // Too many zeros → shrink window
            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }

            // Current valid window
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}