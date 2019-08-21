from dll import DoublyLinkedList


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.root = None

    def insert(self, value):
        # if there is no root node
        if self.root is None:
            # set root node to value
            self.root.add_to_head(value)
        # else there is a root node
        else:
            # if node value is greater than root value
            if self.root.val < node.val:
                # if right root is None
                    # assign value to right root
                # else right root is not None
                    # call insert method with right root and value
                # else node value is less than root value
                # if left root is None
                    # assign value to left root
                # else left root is not None
                    # call insert method with left root and value
        pass

    def contains(self, target):
        if self is None or self.val == target:
            return self

        # if no root or the root is the target
            # return root

        # if root is less than target
            # call contains with right root and target

        # root is greater than target
        # call contains with left root and target

        pass

    def get_max(self):
        pass

    def for_each(self, callback):
        pass
