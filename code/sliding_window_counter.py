import time

class SlidingWindowCounter:
    def __init__(self, window_size_seconds: int = 60, max_requests: int = 100):
        self.window = window_size_seconds
        self.limit = max_requests
        self.prev_count = 0
        self.curr_count = 0
        self.curr_window_start = int(time.time() // self.window) * self.window

    def allow(self) -> bool:
        now = time.time()
        current_window = int(now // self.window) * self.window

        if current_window > self.curr_window_start:
            if current_window == self.curr_window_start + self.window:
                self.prev_count = self.curr_count
            else:
                self.prev_count = 0
            self.curr_count = 0
            self.curr_window_start = current_window

        weight = 1.0 - ((now - self.curr_window_start) / self.window)
        estimated_count = (self.prev_count * weight) + self.curr_count

        if estimated_count < self.limit:
            self.curr_count += 1
            return True
        return False
