import functools

def idempotent_request(cache_client):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            key = request.headers.get("Idempotency-Key")
            if not key:
                return func(request, *args, **kwargs)

            cached = cache_client.get(f"idemp:{key}")
            if cached:
                return cached

            response = func(request, *args, **kwargs)
            cache_client.set(f"idemp:{key}", response, ex=86400)
            return response
        return wrapper
    return decorator
