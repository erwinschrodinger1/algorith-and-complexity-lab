def bruteforce(items, capacity):
    n = len(items)
    best_combination = []
    best_profit = 0

    for i in range(2**n):
        current_combination = []
        current_profit = 0
        current_weight = 0

        for j in range(n):
            if (i >> j) & 1:
                current_combination.append(items[j])
                current_profit += items[j]["profit"]
                current_weight += items[j]["weight"]

        if current_weight <= capacity and current_profit > best_profit:
            best_profit = current_profit
            best_combination = current_combination.copy()

    return best_combination


def greedy(items, capacity):
    for item in items:
        item["p_w_ration"] = item["profit"] / item["weight"]
    sorted_items = sorted(items, key=lambda i: i["p_w_ration"], reverse=True)
    combination = []
    current_weight = 0
    for item in sorted_items:
        if current_weight + item["weight"] < capacity:
            current_weight = current_weight + item["weight"]
            combination.append(
                {
                    "profit": item["profit"],
                    "weight": item["weight"],
                }
            )
        else:
            fraction = capacity - current_weight
            combination.append(
                {
                    "weight": fraction,
                    "profit": item["profit"] * fraction / item["weight"],
                }
            )
            break
    return combination


def dynamic(items, capacity):
    n = len(items)

    dynamic_matrix = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1]["weight"] <= w:
                dynamic_matrix[i][w] = max(
                    dynamic_matrix[i - 1][w],
                    dynamic_matrix[i - 1][w - items[i - 1]["weight"]]
                    + items[i - 1]["profit"],
                )
            else:
                dynamic_matrix[i][w] = dynamic_matrix[i - 1][w]

    selected_items = []
    for i in range(n, 0, -1):
        if dynamic_matrix[i][capacity] != dynamic_matrix[i - 1][capacity]:
            selected_items.append(items[i - 1])
            capacity -= items[i - 1]["weight"]

    return selected_items
