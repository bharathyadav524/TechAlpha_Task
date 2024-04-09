class FibonacciGenerator:
    def __init__(self):
        pass

    def generate_sequence(self, n):
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def generate_custom_range(self, start, end):
        fib_sequence = []
        a, b = 0, 1
        while a < end:
            if a >= start:
                fib_sequence.append(a)
            a, b = b, a + b
        return fib_sequence

    def filter_even(self, sequence):
        return [x for x in sequence if x % 2 == 0]

    def filter_odd(self, sequence):
        return [x for x in sequence if x % 2 != 0]

    def calculate_golden_ratio(self, sequence):
        golden_ratios = [(sequence[i] / sequence[i - 1]) for i in range(2, len(sequence))]
        return golden_ratios

    def visualize_sequence(self, sequence):
        import matplotlib.pyplot as plt
        plt.plot(sequence)
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title('Fibonacci Sequence Visualization')
        plt.show()

# Example usage:
fib_gen = FibonacciGenerator()
fib_sequence = fib_gen.generate_custom_range(0, 100)
print("Fibonacci Sequence (Custom Range):", fib_sequence)
even_sequence = fib_gen.filter_even(fib_sequence)
print("Even Fibonacci Numbers:", even_sequence)
odd_sequence = fib_gen.filter_odd(fib_sequence)
print("Odd Fibonacci Numbers:", odd_sequence)
golden_ratio = fib_gen.calculate_golden_ratio(fib_sequence)
print("Golden Ratio between Consecutive Fibonacci Numbers:", golden_ratio)
fib_gen.visualize_sequence(fib_sequence)
