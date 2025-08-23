/**
 * LeetCode Problem: Two Sum
 * Difficulty: Easy
 * Language: python
 * Problem URL: https://leetcode.com/problems/two-sum/submissions/1745486446/
 * 
 * Auto-committed by LeetUp
 * Date: 2025-08-23T14:34:37.245Z
 */

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myset = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in myset:
                return [idx, myset[comp]]
            else:
                myset[num] = idx
        return None
        
/*
 * End of solution for: Two Sum
 * Committed at: 2025-08-23T14:34:37.245Z
 * 
 * This solution was automatically committed by LeetUp.
 * Visit: https://leetup.app
 */