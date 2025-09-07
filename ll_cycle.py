class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        """Insert node at the end of the linked list"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def create_cycle(self, pos):
        """
        Connect the last node to the node at index 'pos' (0-based).
        If pos = -1, no cycle is created.
        """
        if pos == -1 or not self.head:
            return
        cycle_node = None
        curr = self.head
        index = 0
        while curr.next:
            if index == pos:
                cycle_node = curr
            curr = curr.next
            index += 1
        if cycle_node:
            curr.next = cycle_node  # create cycle

class Solution(object):
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        val = int(input(f"Enter value for node {i+1}: "))
        ll.insert(val)

    pos = int(input("Enter position to connect last node (-1 for no cycle): "))
    ll.create_cycle(pos)

    sol = Solution()
    print("Has cycle?", sol.hasCycle(ll.head))
