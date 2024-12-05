import time
import random
import matplotlib.pyplot as plt
import numpy as np
from MaxSubArray import MaxSubArray


def generateRandom(n):
    return [1] * n
    #return [random.choice(range(-n, 0)) if random.random() < 0.5 else random.choice(range(1, n + 1)) for _ in range(n)]

def main():
    sizes = [1000, 10000, 100000, 1000000, 10000000, 100000000]
    findMax = MaxSubArray()
    random.seed(1)  # For reproducibility

    # Lists to store execution times
    times_divide_conquer = []

    # Header for the results table
    print(f"{'Array Size':>10} | {'Divide & Conquer (s)':>22} ")
    print("-" * 40)

    for size in sizes:
        array = generateRandom(size)

        start_time = time.time()
        max_sum_dc = findMax.findMaxSubArray(array)
        end_time = time.time()
        execution_time_dc = end_time - start_time
        times_divide_conquer.append(execution_time_dc)

        # Print the results in a table row
        print(f"{size:>10} | {execution_time_dc:>22.6f}")

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_divide_conquer, 'o-', label='Divide & Conquer ')

    plt.xlabel('Array Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Maximum Subarray Sum Algorithm Performance')
    plt.legend()
    plt.xscale('log')  # Log scale for better visualization
    plt.yscale('log')  # Log scale to observe linear vs. n log n growth
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()

    # Calculate the slopes in the log-log plot
    log_sizes = np.log(sizes)
    log_times_divide_conquer = np.log(times_divide_conquer)

    # Calculate slope using numpy's polyfit (degree 1 linear fit)
    slope_divide_conquer, intercept = np.polyfit(log_sizes, log_times_divide_conquer, 1)

    print(f"Slope for Divide & Conquer: {slope_divide_conquer:.2f}")


if __name__ == "__main__":
    main()

