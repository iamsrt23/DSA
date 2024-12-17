class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_tail(self):
        # If the list is empty
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        # If the list has only one node
        if self.head.next is None:
            self.head = None
            return

        # Traverse to the second last node
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        # Delete the last node
        temp.next = None

    def printList(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Example usage
if __name__ == "__main__":
    # Create an empty LinkedList
    llist = LinkedList()

    # Insert some elements at the head
    llist.insertAtHead(10)
    llist.insertAtHead(20)
    llist.insertAtHead(30)

    # Print the linked list
    print("Linked List:")
    llist.printList()

    # Delete the tail node
    print("After deleting the tail:")
    llist.delete_tail()
    llist.printList()