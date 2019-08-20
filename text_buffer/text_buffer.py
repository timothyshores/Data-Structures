# Iimplement a text buffer data structure, that could be utilized by the text editors we use everyday, with the following methods:

# ✅ __str__ - Allows us to call print() on our buffer to print out all of its contents
# ✅ append - Adds a character to the back of the text buffer
# ✅ prepend - Adds a character to the front of the text buffer
# ✅ delete_front - Removes a character from the front of the text buffer
# ✅ delete_back - Removes a character from the back of the text buffer
# join - Concatenates another text buffer onto the end of this buffer
# These methods should all be as efficient as possible(we can get most of them down to O(1) time). To achieve this, what data structure(s) would make good candidates for backing our text buffer implementation? An array? A LinkedList? A DoublyLinkedList?

from dll import DoublyLinkedList


class TextBuffer:
    # init is a string we can initalize buffer width
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()

        # if init is not None
        if init:
            # loop through init
            for char in init:
                self.contents.add_to_tail(char)

    def __str__(self):
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, char):
        self.contents.add_to_tail(char)

    def prepend(self, char):
        self.contents.add_to_head(char)

    def delete_front(self, n):
        for _ in range(n):
            self.contents.remove_from_head()

    def delete_back(self, n):
        for _ in range(n):
            self.contents.remove_from_tail()

    def join(self, buffer):
        self.contents.tail.next = buffer.contents.head
        buffer.contents.head.pre = self.contents.tail
        self.contents.tail = buffer.contents.tail


text_buffer1 = TextBuffer("Hello")
text_buffer1.delete_back(2)
print(text_buffer1)
