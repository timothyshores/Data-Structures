from dll import DoublyLinkedList


class LRUCache:
    # Need to store key value pairs. E.g. dictionary
    # Need to track order
    # Need to store cache
    # Need to store cache size
    def __init__(self, limit=10):
        self.cache = DoublyLinkedList()
        self.limit = limit
    """
  Retrieves the value associated with the given key. 
  
  Also moves the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """

    def __str__(self):
        s = ""
        current = self.cache.head
        while current:
            s += str(current.value)
            current = current.next
        return s

    def get(self, key=None):
        node = self.cache.head.value[0]
        while node is not key:
            node = node.next
        return node

        # if str(list(self.cache.head.value)[0]) == str(key):
        #     return "Key found"
        # else:
        #     return "Key not found"

    """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. 
  
  If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. 
  
  Additionally, in the case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """

    def set(self, key, value):
        if len(self.cache) == self.limit:
            self.cache.remove_from_tail()

        self.cache.add_to_head({key, value})


l1 = LRUCache(2)
print(l1)
l1.set("1", "some value 1")
print(l1)
print(l1.get(1))
