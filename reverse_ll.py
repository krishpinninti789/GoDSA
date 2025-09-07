# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr is not None:
            # Save next node
            nxt = curr.next
            # Reverse the link
            curr.next = prev
            # Move prev and curr one step forward
            prev = curr
            curr = nxt

        # prev is the new head
        return prev

# Example usage
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print("Original list:")
printList(head)

sol = Solution()
reversed_head = sol.reverseList(head)

print("Reversed list:")
printList(reversed_head)
