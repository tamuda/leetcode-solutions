/**
 * LeetCode Problem: Rotate List
 * Difficulty: Medium
 * Language: python
 * Problem URL: https://leetcode.com/problems/rotate-list/submissions/1702616402/
 * 
 * Auto-committed by LeetUp
 * Date: 2025-07-18T16:18:32.140Z
 */

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # 1. Get the length and the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Make the list circular
        tail.next = head

        # 3. Find the new tail: (length - k % length - 1)th node
        k = k % length
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # 4. Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
/*
 * End of solution for: Rotate List
 * Committed at: 2025-07-18T16:18:32.140Z
 * 
 * This solution was automatically committed by LeetUp.
 * Visit: https://leetup.app
 */