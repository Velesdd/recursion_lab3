
class Fibonacci:
    fib_cache = {1: 1, 2: 1}

    def find_fibonacci(self, n):
        if Fibonacci.fib_cache.get(n) is None:
            Fibonacci.fib_cache[n] = self.find_fibonacci(n-2)+self.find_fibonacci(n-1)
        return Fibonacci.fib_cache[n]
