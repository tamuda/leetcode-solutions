/**
 * LeetCode Problem: Two Sum
 * Difficulty: Easy
 * Language: python
 * Problem URL: https://leetcode.com/problems/two-sum/
 * 
 * Auto-committed by LeetUp
 * Date: 2025-07-29T12:45:33.267Z
 */

class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}  # Dictionary to store number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i


/*
 * End of solution for: Two Sum
 * Committed at: 2025-07-29T12:45:33.267Z
 * 
 * This solution was automatically committed by LeetUp.
 * Visit: https://leetup.app
 */