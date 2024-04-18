import random
from datetime import datetime
from insertion_sort import insertion_sort
from selection_sort import selection_sort
import matplotlib.pyplot as plt
from tqdm import tqdm

def time_iteration():
    num_values = random.randint(500,5000)
    rand_data = random.sample(range(1,10000),num_values)
    initial_time = datetime.now()
    sorted = insertion_sort(rand_data.copy())
    insertion_time = datetime.now()-initial_time
    initial_time = datetime.now()
    sorted = selection_sort(rand_data.copy())
    selection_time = datetime.now()-initial_time
    return {"num_values":num_values, "insertion_time":insertion_time.total_seconds(),"selection_time":selection_time.total_seconds()}

def main():
    time_list = []
    num_samples = int(input(f"Number of samples:\t"))
    for i in tqdm(range(1,num_samples)):
        time_list.append(time_iteration())

    res = sorted(time_list,key=lambda val:val["num_values"])
    plt.title("Comparision between insertion and selection sort")
    plt.plot([val["num_values"] for val in res],[val["insertion_time"] for val in res],"g")
    plt.plot([val["num_values"] for val in res],[val["selection_time"] for val in res],"b")
    plt.legend(["Selection Sort","Insertion Sort"])
    plt.xlabel("Number of datas")
    plt.ylabel("Time in seconds")
    plt.savefig("graph.png")

if __name__=="__main__":
    main()