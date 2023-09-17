import pytest
from fibonacci.fibonacci_numbers import fibonacci, fibonacci_cached, fibonacci_non_recursive

N = [10, 20, 30]


@pytest.fixture(scope="function", params=N)
def fibonacci_sequence_index(request):
    idx = request.param
    return idx


class TestBenchmarkFibonacciNumbers:
    def test_bm_fibonacci_numbers(self, fibonacci_sequence_index, benchmark):
        print("\nfibonacci:", fibonacci_sequence_index)
        benchmark(fibonacci, fibonacci_sequence_index)

    def test_bm_fibonacci_non_recursive(self, fibonacci_sequence_index, benchmark):
        print("\nfibonacci_non_recursive:", fibonacci_sequence_index)
        benchmark(fibonacci_non_recursive, fibonacci_sequence_index)

    def test_bm_fibonacci_cached(self, fibonacci_sequence_index, benchmark):
        print("\nfibonacci_cached:", fibonacci_sequence_index)
        benchmark(fibonacci_cached, fibonacci_sequence_index)
        fibonacci_cached.cache_clear()
