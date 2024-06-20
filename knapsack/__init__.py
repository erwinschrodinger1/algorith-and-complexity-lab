from knapsack import bruteforce, greedy


def main():
    input_value = [
        {"weight": 10, "profit": 20},
        {"weight": 20, "profit": 10},
        {"weight": 30, "profit": 50},
    ]
    input_capacity = 28
    knack_output = greedy(input_value, input_capacity)
    print(knack_output)


if __name__ == "__main__":
    main()
