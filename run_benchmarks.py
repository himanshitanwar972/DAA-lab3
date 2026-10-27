import os
import random
import pandas as pd

from algorithms.fractional_knapsack import fractional_knapsack
from algorithms.activity_selection import activity_selection
from algorithms.huffman_coding import huffman_encode
from benchmarking.benchmark import measure_performance


# Create the results folder if it does not exist
os.makedirs("results", exist_ok=True)


# Generate random items for Fractional Knapsack
def generate_knapsack_items(n):
    items = []

    for i in range(n):
        item = {
            "name": f"Item{i}",
            "weight": random.randint(1, 100),
            "value": random.randint(10, 500)
        }

        items.append(item)

    return items


# Generate random activities for Activity Selection
def generate_activities(n):
    activities = []

    for i in range(n):
        start = random.randint(0, n * 2)
        duration = random.randint(1, 10)

        activity = {
            "name": f"A{i}",
            "start": start,
            "finish": start + duration
        }

        activities.append(activity)

    return activities


# Generate text for Huffman Coding
def generate_text(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    return "".join(
        random.choice(alphabet) for _ in range(n)
    )


def main():

    # Different input sizes for benchmarking
    input_sizes = [100, 500, 1000, 5000]

    results = []

    for n in input_sizes:

        print(f"\nBenchmarking input size: {n}")

        # ----------------------------------
        # 1. Fractional Knapsack
        # ----------------------------------

        items = generate_knapsack_items(n)
        capacity = n * 25

        time_taken, memory_used = measure_performance(
            fractional_knapsack,
            items,
            capacity,
            repeats=5
        )

        results.append({
            "Algorithm": "Fractional Knapsack",
            "Input Size": n,
            "Execution Time (seconds)": time_taken,
            "Peak Traced Memory (KiB)": memory_used
        })

        # ----------------------------------
        # 2. Activity Selection
        # ----------------------------------

        activities = generate_activities(n)

        time_taken, memory_used = measure_performance(
            activity_selection,
            activities,
            repeats=5
        )

        results.append({
            "Algorithm": "Activity Selection",
            "Input Size": n,
            "Execution Time (seconds)": time_taken,
            "Peak Traced Memory (KiB)": memory_used
        })

        # ----------------------------------
        # 3. Huffman Coding
        # ----------------------------------

        text = generate_text(n)

        time_taken, memory_used = measure_performance(
            huffman_encode,
            text,
            repeats=5
        )

        results.append({
            "Algorithm": "Huffman Coding",
            "Input Size": n,
            "Execution Time (seconds)": time_taken,
            "Peak Traced Memory (KiB)": memory_used
        })

    # Convert results into a DataFrame
    df = pd.DataFrame(results)

    # Save results to a CSV file
    output_file = "results/benchmark_results.csv"

    df.to_csv(output_file, index=False)

    # Display results
    print("\n========== BENCHMARK RESULTS ==========\n")
    print(df.to_string(index=False))

    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()