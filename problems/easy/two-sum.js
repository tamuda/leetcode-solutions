/**
 * LeetCode Problem: Two Sum
 * Difficulty: Easy
 * Language: javascript
 * Problem URL: https://leetcode.com/problems/two-sum/
 * 
 * Auto-committed by LeetUp
 * Date: 2025-07-12T22:14:16.396Z
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Notes: Using HashMap to store complements
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        
        map.set(nums[i], i);
    }
    
    return [];
};
/*
 * End of solution for: Two Sum
 * Committed at: 2025-07-12T22:14:16.396Z
 * 
 * This solution was automatically committed by LeetUp.
 * Visit: https://leetup.app
 */