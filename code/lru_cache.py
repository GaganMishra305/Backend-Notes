class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def _insert(self, node: Node):
        p, n = self.tail.prev, self.tail
        p.next = n.prev = node
        node.prev, node.next = p, n

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
        if len(self.cache) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
