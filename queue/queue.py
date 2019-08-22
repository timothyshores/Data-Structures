from dll import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, item):  # add an item to the back of the queue
        self.size += 1
        self.storage.add_to_tail(item)

    # remove and return an item from the front of the queue
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
        else:
            return None
        return self.storage.remove_from_head()

    # accessor or getter
    # to modify these values we could create setters or mutators
    def len(self):
        return self.size
