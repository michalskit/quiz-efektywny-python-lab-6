# tests quiz lab6

import unittest
from lab6_quiz import conditional_decorator, simple_cache_system, nth_prime
import time

class TestQuiz(unittest.TestCase):
    def test_conditional_decorator_true_condition(self):
        def some_decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs) * 2
            return wrapper

        @conditional_decorator(lambda x: x > 10, some_decorator)
        def test_func(x):
            return x

        self.assertEqual(test_func(5), 5)
        self.assertEqual(test_func(15), 30)

    def test_conditional_decorator_false_condition(self):
        def some_decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs) * 2
            return wrapper

        @conditional_decorator(lambda x: x < 10, some_decorator)
        def test_func(x):
            return x

        self.assertEqual(test_func(5), 10)
        self.assertEqual(test_func(15), 15)

    def test_cache_decorator(self):
        # Using the provided cached_heavy_computation function
        @simple_cache_system(4)
        def cached_heavy_computation(x):
            start_time = time.time()
            _ = nth_prime(x)
            execution_time = time.time() - start_time
            return execution_time

        # First call should compute the result
        exec_time_first_call = cached_heavy_computation(10000)
        self.assertGreater(exec_time_first_call, 0, "Execution time should be non-zero for first call")

        # Second call should retrieve the result from cache, hence expected to be faster or equal
        exec_time_second_call = cached_heavy_computation(10000)
        self.assertLessEqual(exec_time_second_call, exec_time_first_call, "Execution time should be less or equal for cached call")

        # Sleep to expire the cache
        time.sleep(5)

        # Third call after cache expiration, times should be almost equal
        exec_time_third_call = cached_heavy_computation(10000)
        self.assertAlmostEqual(exec_time_third_call, exec_time_first_call, delta=1)


if __name__ == '__main__':
    unittest.main()
