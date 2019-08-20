from dll import DoublyLinkedList


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
