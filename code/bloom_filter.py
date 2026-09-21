import math
import hashlib

class BloomFilter:
    def __init__(self, expected_elements: int, false_positive_rate: float):
        self.size = int(- (expected_elements * math.log(false_positive_rate)) / (math.log(2) ** 2))
        self.hash_count = int((self.size / expected_elements) * math.log(2))
        self.bit_array = [0] * self.size

    def _hashes(self, item: str):
        for i in range(self.hash_count):
            h = hashlib.sha256(f"{item}_{i}".encode()).hexdigest()
            yield int(h, 16) % self.size

    def add(self, item: str):
        for pos in self._hashes(item):
            self.bit_array[pos] = 1

    def __contains__(self, item: str) -> bool:
        return all(self.bit_array[pos] == 1 for pos in self._hashes(item))
