"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:  # if there's no head or tail. E.g. the list is empty
            self.head = new_node
            self.head.prev = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_from_head(self):
        self.delete(self.head)

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:  # if there's no head or tail. E.g. the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def remove_from_tail(self):
        self.delete(self.tail)

    def move_to_front(self, node):
        if node is self.head:
            return

        value = node.value

        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

        self.add_to_head

    def move_to_end(self, node):
        if node is self.tail:
            return

        value = node.value

        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            node.delete()
            self.length -= 1
            self.add_to_tail(value)

    def delete(self, node):
        if not self.head and not self.tail:
            return

        self.length -= 1

        if self.head == self.tail:  # if there's only one node in the list
            self.head = None        # head is none
            self.tail = None  # tail is none
        elif self.head == node:     # if head is the node
            self.head = head.next
            node.delete()
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        pass


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, item):  # add an item to the back of the queue.
        self.size += 1
        self.storage.add_to_tail(item)

    # remove and return an item from the front of the queue.
    def dequeue(self):
        self.size -= 1
        first = self.storage.head

    def len(self):
        return self.size
