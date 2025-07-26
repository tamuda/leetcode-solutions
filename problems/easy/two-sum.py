/**
 * LeetCode Problem: Two Sum
 * Difficulty: Easy
 * Language: python
 * Problem URL: https://leetcode.com/problems/two-sum/submissions/1712164705/
 * 
 * Auto-committed by LeetUp
 * Date: 2025-07-26T13:30:04.222Z
 */

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myset = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in myset:
                return [myset[comp], index]
            else:
                myset[num] = index
        return None
        
/*
 * End of solution for: Two Sum
 * Committed at: 2025-07-26T13:30:04.222Z
 * 
 * This solution was automatically committed by LeetUp.
 * Visit: https://leetup.app
 */