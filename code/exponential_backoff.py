import time
import random

def retry_with_backoff(func, max_attempts=5, base_delay=0.5, max_delay=30.0):
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts:
                raise e
            # Full jitter: random sleep between 0 and min(max_delay, base * 2^attempt)
            sleep_time = random.uniform(0, min(max_delay, base_delay * (2 ** (attempt - 1))))
            time.sleep(sleep_time)
