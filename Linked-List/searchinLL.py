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

    def check_if_present(self, desired_element):
        temp = self.head  # Start from the head of the list

        while temp is not None:
            if temp.data == desired_element:
                return True
            temp = temp.next

        return False

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

    # Check if an element is present
    element = 20
    if llist.check_if_present(element):
        print(f"Element {element} is present in the linked list.")
    else:
        print(f"Element {element} is not present in the linked list.")