class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def lengthOfLL(self):
        count = 0
        temp = self.head  # Start from the head of the list

        while temp is not None:
            count += 1
            temp = temp.next

        return count

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Example usage
if __name__ == "__main__":
    llist = LinkedList()

    # Insert elements into the linked list
    llist.insertAtHead(10)
    llist.insertAtHead(20)
    llist.insertAtHead(30)

    # Print the linked list
    print("Linked List:")
    llist.printList()

    # Find and print the length of the linked list
    print("Length of Linked List:", llist.lengthOfLL())