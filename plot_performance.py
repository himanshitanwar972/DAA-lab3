import os
import pandas as pd
import matplotlib.pyplot as plt

# Create the graphs folder if it does not exist
os.makedirs("graphs", exist_ok=True)

# Load benchmark results
df = pd.read_csv("results/benchmark_results.csv")


# ==========================================
# Graph 1: Execution Time Comparison
# ==========================================

plt.figure(figsize=(10, 6))

for algorithm in df["Algorithm"].unique():
    subset = df[df["Algorithm"] == algorithm]

    plt.plot(
        subset["Input Size"],
        subset["Execution Time (seconds)"],
        marker="o",
        label=algorithm
    )

plt.xlabel("Input Size")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Greedy Algorithms: Execution Time Comparison")
plt.legend()
plt.grid(True)

plt.savefig(
    "graphs/performance_time.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Graph 2: Memory Usage Comparison
# ==========================================

plt.figure(figsize=(10, 6))

for algorithm in df["Algorithm"].unique():
    subset = df[df["Algorithm"] == algorithm]

    plt.plot(
        subset["Input Size"],
        subset["Peak Traced Memory (KiB)"],
        marker="o",
        label=algorithm
    )

plt.xlabel("Input Size")
plt.ylabel("Peak Traced Memory (KiB)")
plt.title("Greedy Algorithms: Memory Usage Comparison")
plt.legend()
plt.grid(True)

plt.savefig(
    "graphs/performance_memory.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()
plt.close()

print("Performance graphs saved successfully!")
print("Check the graphs folder.")