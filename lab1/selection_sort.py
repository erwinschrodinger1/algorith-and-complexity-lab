# function selection sort
# input_arr -> input array (pass by reference)
def selection_sort(input_arr):
    for i in range(len(input_arr)-1):
        min_idx = i
        for j in range(i+1, len(input_arr)):
            if input_arr[min_idx] > input_arr[j]:
                min_idx = j
                       
        input_arr[i], input_arr[min_idx] = input_arr[min_idx], input_arr[i]
    return input_arr