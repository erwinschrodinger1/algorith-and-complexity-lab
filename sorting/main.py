import random
from datetime import datetime
import matplotlib.pyplot as plt
from tqdm import tqdm
import sys
from lab1.insertion_sort import insertion_sort
from lab1.selection_sort import selection_sort
from lab2.quick_sort import quick_sort
from lab2.merge_sort import merge_sort

# Set the recursion limit to a higher value
sys.setrecursionlimit(5000)  # Change 5000 to whatever value you need


def time_iteration():
    num_values = random.randint(500, 5000)
    rand_data = random.sample(range(1, 10000), num_values)

    initial_time = datetime.now()
    sorted_data = insertion_sort(rand_data.copy())
    insertion_time = datetime.now() - initial_time

    initial_time = datetime.now()
    sorted_data = selection_sort(rand_data.copy())
    selection_time = datetime.now() - initial_time

    initial_time = datetime.now()
    sorted_data = merge_sort(rand_data.copy(), 0, len(rand_data) - 1)
    merge_time = datetime.now() - initial_time

    initial_time = datetime.now()
    sorted_data = quick_sort(rand_data.copy(), 0, len(rand_data) - 1)
    quick_time = datetime.now() - initial_time

    return {
        "num_values": num_values,
        "insertion_time": insertion_time.total_seconds(),
        "selection_time": selection_time.total_seconds(),
        "merge_time": merge_time.total_seconds(),
        "quick_time": quick_time.total_seconds(),
    }


def main():
    time_list = []
    num_samples = int(input("Number of samples:\t"))

    for _ in tqdm(range(num_samples)):
        time_list.append(time_iteration())

    res = sorted(time_list, key=lambda val: val["num_values"])

    plt.title("Comparison between insertion, selection, merge, and quick sort")
    plt.plot(
        [val["num_values"] for val in res], [val["insertion_time"] for val in res], "g"
    )
    plt.plot(
        [val["num_values"] for val in res], [val["selection_time"] for val in res], "b"
    )
    plt.plot(
        [val["num_values"] for val in res], [val["merge_time"] for val in res], "r"
    )
    plt.plot(
        [val["num_values"] for val in res], [val["quick_time"] for val in res], "y"
    )

    plt.legend(
        [
            "Insertion Sort",
            "Selection Sort",
            "Merge Sort",
            "Quick Sort",
        ]
    )
    plt.xlabel("Number of data points")
    plt.ylabel("Time in seconds")
    plt.savefig("graph.png")
    plt.show()


if __name__ == "__main__":
    main()
