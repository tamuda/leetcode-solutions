/**
 * LeetCode Problem: Two Sum
 * Difficulty: Easy
 * Language: python
 * Problem URL: https://leetcode.com/problems/two-sum/submissions/1783720308/
 * 
 * Auto-committed by LeetUp
 * Date: 2025-09-26T23:16:36.143Z
 */

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #hashmap
        #iterate the list
        # calc comp in each loop
        # and if comp in set, return 
        myset = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in myset:
                return [myset[comp], idx]
            myset[num] = idx
        return []
        
/*
 * End of solution for: Two Sum
 * Committed at: 2025-09-26T23:16:36.143Z
 * 
 * This solution was automatically committed by LeetUp.
 * Visit: https://leetup.app
 */