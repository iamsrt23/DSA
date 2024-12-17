class Node:

    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class LinkedList:
#Function to Print the Linked List
    def __init__ (self):
       self.head = None

    def insertAtHead(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
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