/**
 * LeetCode Problem: Two Sum
 * Difficulty: Easy
 * Language: python
 * Problem URL: https://leetcode.com/problems/two-sum/submissions/1715150088/
 * 
 * Auto-committed by LeetUp
 * Date: 2025-07-29T00:08:30.399Z
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
 * Committed at: 2025-07-29T00:08:30.399Z
 * 
 * This solution was automatically committed by LeetUp.
 * Visit: https://leetup.app
 */