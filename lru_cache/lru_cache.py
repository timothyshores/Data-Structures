class LRUCache:
    # Need to store key value pairs. E.g. dictionary
    # Need to track order
    # Need to store cache
    # Need to store cache size
    def __init__(self, limit=10):
        self.cache = DoublyLinkedList()
        self.limit = limit

    def __repr__(self):
        return f"self.contents: {self.contents}"

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """

    def get(self, key=None):
        return self.cache

    """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """

    def set(self, key, value):
        self.cache.add_to_head({key, value})
        # self.contents = [{key, value}] + self.contents

        # if (len(self.contents) >= self.limit):
        #     del self.contents[-1]


l1 = LRUCache()
l1.set("some key 1", "some value 1")
print(l1)
