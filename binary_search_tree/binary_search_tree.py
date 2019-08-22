from dll import DoublyLinkedList


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.root = None

    def insert(self, value):
        # value is less than root, move left
        if value < self.value:
            # if there's no left node
            if not self.left:
                # create a new leaf to the left with value
                self.left = BinarySearchTree(value)
            # else there is a left node
            else:
                # compare to self.left.value
                self.left.insert(value)
        else:
            # if there's no right node
            if not self.right:
                # create a new leaf to the right with value
                self.right = BinarySearchTree(value)
            # else there is a right node
            else:
                # compare to self.right.value
                self.right.insert(value)

    def contains(self, target):
        # if target is less than node
        if target < self.value:
            # left node does not exist
            if not self.left:
                return False
            # left node exists
            else:
                # call method with left node
                return self.left.contains(target)
        # target is equal to or greater than node
        else:
            # right node does not exist
            if not self.right:
                return True
            # right node exists
            else:
                # call method with right node
                return self.right.contains(target)

    # go right until your find the largest value
    def get_max(self):
        # if BST is empty
        if not self:
            return None
        # if BST is not empty
        else:
            # if right node is null
            if not self.right:
                # return current value
                return self.value
            # else right node exists
            else:
                # keep going right
                return self.get_max()

    def get_max_solution_2(self):
        # if there's no right node
        if not self.right:
            # return current node
            return self.value
        # continue moving right until right node is null
        return self.right.get_max()

    def for_each(self, callback):
        # traverse tree

        callback(self.value)
        if self.left:
            self.left.for_each(callback)
        if self.right:
            self.right.for_each(callback)

    def unorder_print():
        for_each(print(self.value))


bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
def cb(x): return print(x)
