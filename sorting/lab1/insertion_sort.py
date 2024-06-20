# function to sort data using insertion_sort
# input_arr -> input array (pass by reference)
def insertion_sort(input_arr: list):
    for i in range(1, len(input_arr)):
        key = input_arr[i]
        j = i - 1
        while j >= 0 and key < input_arr[j]:
            input_arr[j + 1] = input_arr[j]
            j -= 1
        input_arr[j + 1] = key

    return input_arr.copy()
