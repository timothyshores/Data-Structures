class Heap:
    def __init__(self):
        self.storage = []

    def __str__(self):
        return '[' + ', '.join(self.storage) + ']'

    def insert(self, value):
        # add new value to end of list
        self.storage.append(value)

        self._bubble_up(self.storage, self.get_size() - 1)

    def delete(self):
        if self.get_size == 0:
            return None
        pass

    def get_max(self):
        if self.get_size == 0:
            return None
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    # helper method to compare current node to parent node
    def _bubble_up(self, index):
        # parent index
        parent_index = index - 1 // 2

        if parent_idx < 0:
            return

        # current node is larger than parent
        if self.storage[index] > self.storage[parent_index]:
            # swap current node with parent
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            # continue continue to bubble up
            self._bubble_up(self.storage, parent_index)

    # helper method to compare current node to child node

    def _sift_down(self, index):
        # child index
        child_index = 2 * index + 1

        # if index is greater than len(self.storage)
        if child_index > self.get_size():
            return

        # if a node has both a left child and right child
        if child_index + 1 < self.get_size() and self.heap[child_index] < self.heap[child_index + 1]:
            # compare to larger child
            child_index += 1

        # if child node is greater than current node
        if self.heap[child_index] > self.heap[index]:
            # swap
            self.storage[index], self.storage[child_index] = self.storage[child_index], self.storage[index]
            # continue continue to sift down
            self._bubble_up(self.storage, child_index)

    # strech task return get_size using tree traversal


h = Heap()
print(h.insert('a'))
print(h.insert('b'))
print(h.insert('c'))
print(h)
print(h.get_size())
