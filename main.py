class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_last_node_in_cycle(head):
    # Initialize two pointers: slow and fast, both starting at the head of the linked list
    slow = head
    fast = head

    # Move slow pointer by one step and fast pointer by two steps to detect a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If slow and fast pointers meet, a cycle is detected
        if fast == slow:
            break
    else:
        # If no cycle is detected (fast reaches the end of the list), return None
        return None

    # Reset slow pointer to the head of the list
    slow = head

    # Move both pointers one step at a time until they meet again
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # When slow and fast pointers meet, they are at the start of the cycle
    return slow.value  # Return the value of the node where the cycle starts

# Creating nodes for the linked list
num1 = Node(100)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)

# Setting up the next pointers to create a cycle in the list
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num3  # This creates a cycle that starts at num3 (node with value 3)

# Finding and printing the value of the node where the cycle starts
print(find_last_node_in_cycle(num1))  # Output: 3
