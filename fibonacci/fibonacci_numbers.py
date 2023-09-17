from functools import lru_cache

class InvalidSequenceIndex(Exception):
    pass


def fibonacci(n: int) -> int:
    if n < 0:
        raise InvalidSequenceIndex
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def fibonacci_non_recursive(n: int) -> int:
    if n < 0:
        raise InvalidSequenceIndex
    if n == 0 or n == 1:
        return n
    else:
        v1 = 0
        v2 = 1
        current_index = 1
        while n  > current_index:
            current_index += 1
            v1, v2 = v2, v1+v2
        return v2


@lru_cache(maxsize=2)
def fibonacci_cached(n: int) -> int:
    if n < 0:
        raise InvalidSequenceIndex
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_cached(n-2) + fibonacci_cached(n-1)


if __name__ == "__main__":
    result = fibonacci_non_recursive(6)
    print(result)
