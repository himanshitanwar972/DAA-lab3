import os
import pandas as pd

# Create the results folder if it does not exist
os.makedirs("results", exist_ok=True)

# Theoretical complexity information
data = [
    {
        "Algorithm": "Fractional Knapsack",
        "Theoretical Time Complexity": "O(n log n)",
        "Auxiliary Space Complexity": "O(n)",
        "Reason": "Sorting items by value-to-weight ratio"
    },
    {
        "Algorithm": "Activity Selection",
        "Theoretical Time Complexity": "O(n log n)",
        "Auxiliary Space Complexity": "O(n)",
        "Reason": "Sorting activities by finish time"
    },
    {
        "Algorithm": "Huffman Coding",
        "Theoretical Time Complexity": "O(L + k log k)",
        "Auxiliary Space Complexity": "O(k + L)",
        "Reason": "Frequency counting, heap operations and encoding"
    }
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Save the table as a CSV file
output_file = "results/complexity_comparison.csv"
df.to_csv(output_file, index=False)

# Display the table
print("\n========== COMPLEXITY COMPARISON ==========\n")
print(df.to_string(index=False))

print(f"\nComplexity table saved to: {output_file}")