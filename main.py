from algorithms.fractional_knapsack import fractional_knapsack

items = [
    {"name": "Gold", "weight": 10, "value": 60},
    {"name": "Silver", "weight": 20, "value": 100},
    {"name": "Bronze", "weight": 30, "value": 120}
]

value, weight, selected = fractional_knapsack(items, 50)

print("Maximum value:", value)
print("Total weight:", weight)

for item in selected:
    print(item)


from algorithms.activity_selection import activity_selection

activities = [
    {"name": "A1", "start": 1, "finish": 4},
    {"name": "A2", "start": 3, "finish": 5},
    {"name": "A3", "start": 0, "finish": 6},
    {"name": "A4", "start": 5, "finish": 7},
    {"name": "A5", "start": 3, "finish": 9},
    {"name": "A6", "start": 5, "finish": 9},
    {"name": "A7", "start": 6, "finish": 10},
    {"name": "A8", "start": 8, "finish": 11}
]

selected = activity_selection(activities)

print("Selected activities:")

for activity in selected:
    print(
        activity["name"],
        activity["start"],
        activity["finish"]
    )

print("Total selected:", len(selected))


from algorithms.huffman_coding import huffman_encode

text = "abracadabra"

result = huffman_encode(text)

print("Frequencies:", result["frequencies"])
print("Huffman codes:", result["codes"])
print("Encoded output:", result["encoded"])
print("Original bits:", result["original_bits"])
print("Encoded bits:", result["encoded_bits"])

print(
    "Compression ratio:",
    f'{result["compression_ratio"]:.2%}'
)

print(
    "Space saved:",
    f'{result["space_saved_percent"]:.2f}%'
)