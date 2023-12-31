"""
Write a function, linked_palindrome, that takes in the head of a linked list as an argument. The function should return
a boolean indicating whether or not the linked list is a palindrome.
A palindrome is a sequence that is the same both forwards and backwards.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_palindrome(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next

    return values == values[::-1]


a = Node(3)
b = Node(2)
c = Node(7)
d = Node(7)
e = Node(2)
f = Node(3)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 3 -> 2 -> 7 -> 7 -> 2 -> 3
assert linked_palindrome(a) is True

# n = number of nodes
# Time: O(n)
# Space: O(n)
