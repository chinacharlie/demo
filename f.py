import functools

@functools.lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
         return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(40))

