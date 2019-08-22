from dll import DoublyLinkedList


class LRUCache:
    # Need to store key value pairs. E.g. dictionary
    # Need to track order
    # Need to store cache
    # Need to store cache size
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = dict()
        self.order = DoublyLinkedList()

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
        # Case: key is not present
        if key in self.storage:
            # Move retrieved item to head
            node = self.storage[key]
            self.order.move_to_front(node)
        # Return value for a given key
            return node.value[1]

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
        if key in key.self.cache:
            node = self.cache[key]
            node.value = (key, value)
            self.order.move_to_front()
            return

        if self.size == self.limit:
            del self.storage[self.order.tail.value[0]]
            self.cache.remove_from_tail()
            self.size -= 1

        self.order.add_to_head((key, value))
        self.storage(key) = self.order.head
        self.size += 1


my_lru = LRUCache(3)

my_lru.set("first", "a")
my_lru.set("second", "b")
my_lru.set("third", "c")
my_lru.set("fourth", "d")
