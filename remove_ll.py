class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")


class Solution(object):
    def removeElements(self, head, val):
        temp = ListNode(0)   # dummy node
        temp.next = head
        prev, curr = temp, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return temp.next


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        val = int(input(f"Enter value for node {i+1}: "))
        ll.insert(val)

    print("Original Linked List:")
    ll.display()

    x = int(input("Enter value to remove: "))
    sol = Solution()
    ll.head = sol.removeElements(ll.head, x)

    print("After removing elements:")
    ll.display()
