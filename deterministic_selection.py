def deterministic_select(arr, k):
    def partition(arr, low, high, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        store_index = low
        for i in range(low, high):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1
        arr[store_index], arr[high] = arr[high], arr[store_index]
        return store_index

    def select_helper(arr, k):
        if len(arr) <= 5:
            return sorted(arr)[k]

        # Divide array into groups of 5
        sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
        medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
        median_of_medians = select_helper(medians, len(medians) // 2)

        pivot_index = arr.index(median_of_medians)
        pivot_new_index = partition(arr, 0, len(arr) - 1, pivot_index)

        if k < pivot_new_index:
            return select_helper(arr[:pivot_new_index], k)
        elif k > pivot_new_index:
            return select_helper(arr[pivot_new_index + 1:], k - pivot_new_index - 1)
        else:
            return arr[pivot_new_index]

    return select_helper(arr, k)


