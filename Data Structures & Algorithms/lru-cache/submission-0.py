class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev
    
    def append(self, node):
        prev = self.tail.prev
        prev.nxt = node
        self.tail.prev = node

        node.prev = prev
        node.nxt = self.tail


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.append(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.append(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.nxt
            self.remove(lru)
            del self.cache[lru.key]