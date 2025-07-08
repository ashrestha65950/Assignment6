import time
import random
from deterministic_selection import deterministic_select  # Median of Medians
from randomized_selection import quickselect  # Quickselect

def run_test(algorithm, arr, k):
    """Times how long it takes to run the selection algorithm."""
    start = time.time()
    result = algorithm(arr.copy(), k)
    end = time.time()
    return result, end - start

def run_experiments():
    sizes = [1000, 5000, 10000]
    distributions = ["random", "sorted", "reverse"]

    for size in sizes:
        for dist in distributions:
            # Generate the input array
            if dist == "random":
                array = random.sample(range(size * 10), size)
            elif dist == "sorted":
                array = list(range(size))
            elif dist == "reverse":
                array = list(range(size, 0, -1))

            k = size // 2  # Middle element

            # Time deterministic (Median of Medians)
            det_result, time_det = run_test(lambda a, k: deterministic_select(a, k), array, k)

            # Time randomized (Quickselect)
            rand_result, time_rand = run_test(lambda a, k: quickselect(a, 0, len(a) - 1, k), array, k)

            # Output results
            print(f"--- Size: {size}, Distribution: {dist} ---")
            print(f"Deterministic result: {det_result}, Time: {time_det:.6f} seconds")
            print(f"Randomized   result: {rand_result}, Time: {time_rand:.6f} seconds")
            print()

if __name__ == "__main__":
    run_experiments()

