/**
 * LeetCode Problem: Rotate List
 * Difficulty: Medium
 * Language: python
 * Problem URL: https://leetcode.com/problems/rotate-list/
 * 
 * Auto-committed by LeetUp
 * Date: 2025-07-17T22:33:23.699Z
 */

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self,head, k):
        if not head or not head.next or k == 0:
            return head  # Nothing to rotate

        # Step 1: Count the length and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Make the list circular
        tail.next = head

        # Step 3: Find the new tail (length - k % length - 1 steps ahead)
        k = k % length
        steps_to_new_tail = length - k

        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # Step 4: Set new head and break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head

/*
 * End of solution for: Rotate List
 * Committed at: 2025-07-17T22:33:23.699Z
 * 
 * This solution was automatically committed by LeetUp.
 * Visit: https://leetup.app
 */