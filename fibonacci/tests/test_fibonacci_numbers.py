import pytest
from fibonacci.fibonacci_numbers import fibonacci, fibonacci_cached, fibonacci_non_recursive

known_fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]


@pytest.fixture(scope="function", params=enumerate(known_fibonacci_numbers))
def known_fibonacci(request):
    idx, value = request.param
    return idx, value


class TestFibonacciNumbers:
    def test_fibonacci_numbers(self, known_fibonacci):
        n, expected_value = known_fibonacci
        assert fibonacci(n) == expected_value

    def test_fibonacci_numbers_non_recursive(self, known_fibonacci):
        n, expected_value = known_fibonacci
        assert fibonacci_non_recursive(n) == expected_value

    def test_fibonacci_numbers_cached(self, known_fibonacci):
        n, expected_value = known_fibonacci
        assert fibonacci_cached(n) == expected_value


