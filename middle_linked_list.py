class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Print the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Find the middle node
    def middleNode(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    ll = LinkedList()
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        val = int(input(f"Enter value for node {i+1}: "))
        ll.insert(val)

    print("Linked List:")
    ll.display()

    mid = ll.middleNode()
    if mid:
        print("Middle Node:", mid.data)
    else:
        print("The list is empty.")
