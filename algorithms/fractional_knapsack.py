def fractional_knapsack(items, capacity):
    """
    Select items to maximize total value.
    Fractions of items are allowed.
    """

    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")

    if any(
        item["weight"] <= 0 or item["value"] < 0
        for item in items
    ):
        raise ValueError(
            "Weights must be positive and values non-negative."
        )

    # Sort by value-to-weight ratio in descending order.
    sorted_items = sorted(
        items,
        key=lambda item: item["value"] / item["weight"],
        reverse=True
    )

    total_value = 0.0
    total_weight = 0.0
    remaining = capacity
    selected = []

    for item in sorted_items:
        if remaining <= 0:
            break

        weight = item["weight"]
        value = item["value"]

        if weight <= remaining:
            fraction = 1.0
        else:
            fraction = remaining / weight

        allocated_weight = weight * fraction
        allocated_value = value * fraction

        selected.append({
            "name": item["name"],
            "fraction": fraction,
            "weight": allocated_weight,
            "value": allocated_value
        })

        total_weight += allocated_weight
        total_value += allocated_value
        remaining -= allocated_weight

    return total_value, total_weight, selected


