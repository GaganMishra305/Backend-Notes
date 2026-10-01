import queue
import time

class SimpleConnectionPool:
    def __init__(self, factory, max_connections: int = 10):
        self.factory = factory
        self.max_connections = max_connections
        self.pool = queue.Queue(maxsize=max_connections)
        self.created = 0

    def acquire(self):
        if not self.pool.empty() or self.created >= self.max_connections:
            return self.pool.get()
        self.created += 1
        return self.factory()

    def release(self, conn):
        self.pool.put(conn)
