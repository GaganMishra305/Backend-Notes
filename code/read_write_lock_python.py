import threading

class RWLock:
    def __init__(self):
        self._readers = 0
        self._lock = threading.Lock()
        self._writers_lock = threading.Lock()

    def acquire_read(self):
        with self._lock:
            self._readers += 1
            if self._readers == 1:
                self._writers_lock.acquire()

    def release_read(self):
        with self._lock:
            self._readers -= 1
            if self._readers == 0:
                self._writers_lock.release()

    def acquire_write(self):
        self._writers_lock.acquire()

    def release_write(self):
        self._writers_lock.release()
